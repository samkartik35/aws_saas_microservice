    
from __future__ import absolute_import

import inspect
import sys


KAFKA_SERVER ='192.168.43.231:9092'
KAFKA_DATA_TOPIC ='data_queue'
KAFKA_CONTROL_TOPIC = 'control_queue'
KAFKA_CONTROL_DATA_TOPIC = 'control_data_topic'


''' Initialise Kafka Queue 
	configure Kafka environment
	pip install kafka-python
	insure to import libraries required for Kafka
	Create Data and Control topics
	kafka-topics.bat --create --zookeeper localhost:2181 
	--replication-factor 1 --partitions 1 --topic numtest
	from time import sleep
	from json import dumps
	from kafka import KafkaProducer
'''
''' Creating Consumers for data topics'''
def initialiseKafkaConsumers(ServiceID,KAFKA_SERVER):
    KAFKA_DATA_TOPIC = ServiceID +"data"
    KAFKA_CONTROL_TOPIC = ServiceID +"control"
    
    consumerData = KafkaConsumer(
        KAFKA_DATA_TOPIC,
        bootstrap_servers=[KAFKA_SERVER],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))
   
    consumerControl = KafkaConsumer(
        KAFKA_CONTROL_TOPIC,
        bootstrap_servers=[KAFKA_SERVER],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))
   
    consumer_ControlData = KafkaConsumer(
        KAFKA_CONTROL_DATA_TOPIC,
        bootstrap_servers=[KAFKA_SERVER],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    return(consumerData,Consumer_Control,Consumer_ControlData)


def send_messages(self, topic, value=None, **kwargs):
        """
        Publish messages to the desired topic
        Arguments:
          topic(str): topic name to publish messages
          partition(int): partition nubmer
          key(str): key name
          value(str): message to publish
        Returns:
          result(bool) : False if exception occures, True otherwise
        """
        partition = kwargs.get("partition", None)
        headers = kwargs.get("headers", None)
        timestamp = kwargs.get("timestamp", None)
        key = kwargs.get("key", None)
        print_info("publishing messages to the topic")
        try:
            self.kafka_producer.send(topic=topic,
                                     value=value,
                                     partition=partition,
                                     key=key,
                                     headers=headers,
                                     timestamp_ms=timestamp)
            self.kafka_producer.flush()
            result = True
        except KafkaError as exc:
            print_error("Exception during publishing messages - {}".format(exc))
            result = False
        return result 
    
def listen_for_messages(msg, consumer, application_source_id):  # noqa: C901
    """
    Listen for Platform-Sources kafka messages.

    Args:
        consumer (Consumer): Kafka consumer object
        application_source_id (Integer): Cost Management's current Application Source ID. Used for
            kafka message filtering.

    Returns:
        None

    """
    try:
        try:
            msg = get_sources_msg_data(msg, application_source_id)
            offset = msg.get("offset")
            partition = msg.get("partition")
        except SourcesMessageError:
            return
        if msg:
            LOG.info(f"Processing message offset: {offset} partition: {partition}")
            topic_partition = TopicPartition(topic=Config.SOURCES_TOPIC, partition=partition, offset=offset)
            LOG.info(f"Cost Management Message to process: {str(msg)}")
            try:
                with transaction.atomic():
                    process_message(application_source_id, msg)
                    consumer.commit()
            except (IntegrityError, InterfaceError, OperationalError) as err:
                connection.close()
                LOG.error(f"{type(err).__name__}: {err}")
                rewind_consumer_to_retry(consumer, topic_partition)
            except SourcesHTTPClientError as err:
                LOG.error(err)
                rewind_consumer_to_retry(consumer, topic_partition)
            except SourceNotFoundError:
                LOG.warning(f"Source not found in platform sources. Skipping msg: {msg}")
                consumer.commit()

    except KafkaError as error:
        LOG.error(f"[listen_for_messages] Kafka error encountered: {type(error).__name__}: {error}", exc_info=True)
    except Exception as error:
        LOG.error(f"[listen_for_messages] UNKNOWN error encountered: {type(error).__name__}: {error}", exc_info=True) 
        

class KafkaError(RuntimeError):
    retriable = False
    # whether metadata should be refreshed on error
    invalid_metadata = False

    def __str__(self):
        if not self.args:
            return self.__class__.__name__
        return '{0}: {1}'.format(self.__class__.__name__,
                               super(KafkaError, self).__str__())


class IllegalStateError(KafkaError):
    pass


class IllegalArgumentError(KafkaError):
    pass


class NoBrokersAvailable(KafkaError):
    retriable = True
    invalid_metadata = True


class NodeNotReadyError(KafkaError):
    retriable = True


class KafkaProtocolError(KafkaError):
    retriable = True


class CorrelationIdError(KafkaProtocolError):
    retriable = True


class Cancelled(KafkaError):
    retriable = True


class TooManyInFlightRequests(KafkaError):
    retriable = True


class StaleMetadata(KafkaError):
    retriable = True
    invalid_metadata = True


class MetadataEmptyBrokerList(KafkaError):
    retriable = True


class UnrecognizedBrokerVersion(KafkaError):
    pass


class IncompatibleBrokerVersion(KafkaError):
    pass


class CommitFailedError(KafkaError):
    def __init__(self, *args, **kwargs):
        super(CommitFailedError, self).__init__(
            """Commit cannot be completed since the group has already
            rebalanced and assigned the partitions to another member.
            This means that the time between subsequent calls to poll()
            was longer than the configured max_poll_interval_ms, which
            typically implies that the poll loop is spending too much
            time message processing. You can address this either by
            increasing the rebalance timeout with max_poll_interval_ms,
            or by reducing the maximum size of batches returned in poll()
            with max_poll_records.
            """, *args, **kwargs)


class AuthenticationMethodNotSupported(KafkaError):
    pass


class AuthenticationFailedError(KafkaError):
    retriable = False


class BrokerResponseError(KafkaError):
    errno = None
    message = None
    description = None

    def __str__(self):
        """Add errno to standard KafkaError str"""
        return '[Error {0}] {1}'.format(
            self.errno,
            super(BrokerResponseError, self).__str__())


class NoError(BrokerResponseError):
    errno = 0
    message = 'NO_ERROR'
    description = 'No error--it worked!'


class UnknownError(BrokerResponseError):
    errno = -1
    message = 'UNKNOWN'
    description = 'An unexpected server error.'


class OffsetOutOfRangeError(BrokerResponseError):
    errno = 1
    message = 'OFFSET_OUT_OF_RANGE'
    description = ('The requested offset is outside the range of offsets'
                   ' maintained by the server for the given topic/partition.')


class CorruptRecordException(BrokerResponseError):
    errno = 2
    message = 'CORRUPT_MESSAGE'
    description = ('This message has failed its CRC checksum, exceeds the'
                   ' valid size, or is otherwise corrupt.')

# Backward compatibility
InvalidMessageError = CorruptRecordException


class UnknownTopicOrPartitionError(BrokerResponseError):
    errno = 3
    message = 'UNKNOWN_TOPIC_OR_PARTITION'
    description = ('This request is for a topic or partition that does not'
                   ' exist on this broker.')
    retriable = True
    invalid_metadata = True


class InvalidFetchRequestError(BrokerResponseError):
    errno = 4
    message = 'INVALID_FETCH_SIZE'
    description = 'The message has a negative size.'


class LeaderNotAvailableError(BrokerResponseError):
    errno = 5
    message = 'LEADER_NOT_AVAILABLE'
    description = ('This error is thrown if we are in the middle of a'
                   ' leadership election and there is currently no leader for'
                   ' this partition and hence it is unavailable for writes.')
    retriable = True
    invalid_metadata = True


class NotLeaderForPartitionError(BrokerResponseError):
    errno = 6
    message = 'NOT_LEADER_FOR_PARTITION'
    description = ('This error is thrown if the client attempts to send'
                   ' messages to a replica that is not the leader for some'
                   ' partition. It indicates that the clients metadata is out'
                   ' of date.')
    retriable = True
    invalid_metadata = True


class RequestTimedOutError(BrokerResponseError):
    errno = 7
    message = 'REQUEST_TIMED_OUT'
    description = ('This error is thrown if the request exceeds the'
                   ' user-specified time limit in the request.')
    retriable = True


class BrokerNotAvailableError(BrokerResponseError):
    errno = 8
    message = 'BROKER_NOT_AVAILABLE'
    description = ('This is not a client facing error and is used mostly by'
                   ' tools when a broker is not alive.')


class ReplicaNotAvailableError(BrokerResponseError):
    errno = 9
    message = 'REPLICA_NOT_AVAILABLE'
    description = ('If replica is expected on a broker, but is not (this can be'
                   ' safely ignored).')


class MessageSizeTooLargeError(BrokerResponseError):
    errno = 10
    message = 'MESSAGE_SIZE_TOO_LARGE'
    description = ('The server has a configurable maximum message size to avoid'
                   ' unbounded memory allocation. This error is thrown if the'
                   ' client attempt to produce a message larger than this'
                   ' maximum.')


class StaleControllerEpochError(BrokerResponseError):
    errno = 11
    message = 'STALE_CONTROLLER_EPOCH'
    description = 'Internal error code for broker-to-broker communication.'


class OffsetMetadataTooLargeError(BrokerResponseError):
    errno = 12
    message = 'OFFSET_METADATA_TOO_LARGE'
    description = ('If you specify a string larger than configured maximum for'
                   ' offset metadata.')


# TODO is this deprecated? https://cwiki.apache.org/confluence/display/KAFKA/A+Guide+To+The+Kafka+Protocol#AGuideToTheKafkaProtocol-ErrorCodes
class StaleLeaderEpochCodeError(BrokerResponseError):
    errno = 13
    message = 'STALE_LEADER_EPOCH_CODE'


class GroupLoadInProgressError(BrokerResponseError):
    errno = 14
    message = 'OFFSETS_LOAD_IN_PROGRESS'
    description = ('The broker returns this error code for an offset fetch'
                   ' request if it is still loading offsets (after a leader'
                   ' change for that offsets topic partition), or in response'
                   ' to group membership requests (such as heartbeats) when'
                   ' group metadata is being loaded by the coordinator.')
    retriable = True


class GroupCoordinatorNotAvailableError(BrokerResponseError):
    errno = 15
    message = 'CONSUMER_COORDINATOR_NOT_AVAILABLE'
    description = ('The broker returns this error code for group coordinator'
                   ' requests, offset commits, and most group management'
                   ' requests if the offsets topic has not yet been created, or'
                   ' if the group coordinator is not active.')
    retriable = True


class NotCoordinatorForGroupError(BrokerResponseError):
    errno = 16
    message = 'NOT_COORDINATOR_FOR_CONSUMER'
    description = ('The broker returns this error code if it receives an offset'
                   ' fetch or commit request for a group that it is not a'
                   ' coordinator for.')
    retriable = True


class InvalidTopicError(BrokerResponseError):
    errno = 17
    message = 'INVALID_TOPIC'
    description = ('For a request which attempts to access an invalid topic'
                   ' (e.g. one which has an illegal name), or if an attempt'
                   ' is made to write to an internal topic (such as the'
                   ' consumer offsets topic).')


class RecordListTooLargeError(BrokerResponseError):
    errno = 18
    message = 'RECORD_LIST_TOO_LARGE'
    description = ('If a message batch in a produce request exceeds the maximum'
                   ' configured segment size.')


class NotEnoughReplicasError(BrokerResponseError):
    errno = 19
    message = 'NOT_ENOUGH_REPLICAS'
    description = ('Returned from a produce request when the number of in-sync'
                   ' replicas is lower than the configured minimum and'
                   ' requiredAcks is -1.')
    retriable = True


class NotEnoughReplicasAfterAppendError(BrokerResponseError):
    errno = 20
    message = 'NOT_ENOUGH_REPLICAS_AFTER_APPEND'
    description = ('Returned from a produce request when the message was'
                   ' written to the log, but with fewer in-sync replicas than'
                   ' required.')
    retriable = True


class InvalidRequiredAcksError(BrokerResponseError):
    errno = 21
    message = 'INVALID_REQUIRED_ACKS'
    description = ('Returned from a produce request if the requested'
                   ' requiredAcks is invalid (anything other than -1, 1, or 0).')


class IllegalGenerationError(BrokerResponseError):
    errno = 22
    message = 'ILLEGAL_GENERATION'
    description = ('Returned from group membership requests (such as heartbeats)'
                   ' when the generation id provided in the request is not the'
                   ' current generation.')


class InconsistentGroupProtocolError(BrokerResponseError):
    errno = 23
    message = 'INCONSISTENT_GROUP_PROTOCOL'
    description = ('Returned in join group when the member provides a protocol'
                   ' type or set of protocols which is not compatible with the'
                   ' current group.')


class InvalidGroupIdError(BrokerResponseError):
    errno = 24
    message = 'INVALID_GROUP_ID'
    description = 'Returned in join group when the groupId is empty or null.'


class UnknownMemberIdError(BrokerResponseError):
    errno = 25
    message = 'UNKNOWN_MEMBER_ID'
    description = ('Returned from group requests (offset commits/fetches,'
                   ' heartbeats, etc) when the memberId is not in the current'
                   ' generation.')


class InvalidSessionTimeoutError(BrokerResponseError):
    errno = 26
    message = 'INVALID_SESSION_TIMEOUT'
    description = ('Return in join group when the requested session timeout is'
                   ' outside of the allowed range on the broker')


class RebalanceInProgressError(BrokerResponseError):
    errno = 27
    message = 'REBALANCE_IN_PROGRESS'
    description = ('Returned in heartbeat requests when the coordinator has'
                   ' begun rebalancing the group. This indicates to the client'
                   ' that it should rejoin the group.')


class InvalidCommitOffsetSizeError(BrokerResponseError):
    errno = 28
    message = 'INVALID_COMMIT_OFFSET_SIZE'
    description = ('This error indicates that an offset commit was rejected'
                   ' because of oversize metadata.')


class TopicAuthorizationFailedError(BrokerResponseError):
    errno = 29
    message = 'TOPIC_AUTHORIZATION_FAILED'
    description = ('Returned by the broker when the client is not authorized to'
                   ' access the requested topic.')


class GroupAuthorizationFailedError(BrokerResponseError):
    errno = 30
    message = 'GROUP_AUTHORIZATION_FAILED'
    description = ('Returned by the broker when the client is not authorized to'
                   ' access a particular groupId.')


class ClusterAuthorizationFailedError(BrokerResponseError):
    errno = 31
    message = 'CLUSTER_AUTHORIZATION_FAILED'
    description = ('Returned by the broker when the client is not authorized to'
                   ' use an inter-broker or administrative API.')


class InvalidTimestampError(BrokerResponseError):
    errno = 32
    message = 'INVALID_TIMESTAMP'
    description = 'The timestamp of the message is out of acceptable range.'


class UnsupportedSaslMechanismError(BrokerResponseError):
    errno = 33
    message = 'UNSUPPORTED_SASL_MECHANISM'
    description = 'The broker does not support the requested SASL mechanism.'


class IllegalSaslStateError(BrokerResponseError):
    errno = 34
    message = 'ILLEGAL_SASL_STATE'
    description = 'Request is not valid given the current SASL state.'


class UnsupportedVersionError(BrokerResponseError):
    errno = 35
    message = 'UNSUPPORTED_VERSION'
    description = 'The version of API is not supported.'


class TopicAlreadyExistsError(BrokerResponseError):
    errno = 36
    message = 'TOPIC_ALREADY_EXISTS'
    description = 'Topic with this name already exists.'


class InvalidPartitionsError(BrokerResponseError):
    errno = 37
    message = 'INVALID_PARTITIONS'
    description = 'Number of partitions is invalid.'


class InvalidReplicationFactorError(BrokerResponseError):
    errno = 38
    message = 'INVALID_REPLICATION_FACTOR'
    description = 'Replication-factor is invalid.'


class InvalidReplicationAssignmentError(BrokerResponseError):
    errno = 39
    message = 'INVALID_REPLICATION_ASSIGNMENT'
    description = 'Replication assignment is invalid.'


class InvalidConfigurationError(BrokerResponseError):
    errno = 40
    message = 'INVALID_CONFIG'
    description = 'Configuration is invalid.'


class NotControllerError(BrokerResponseError):
    errno = 41
    message = 'NOT_CONTROLLER'
    description = 'This is not the correct controller for this cluster.'
    retriable = True


class InvalidRequestError(BrokerResponseError):
    errno = 42
    message = 'INVALID_REQUEST'
    description = ('This most likely occurs because of a request being'
                   ' malformed by the client library or the message was'
                   ' sent to an incompatible broker. See the broker logs'
                   ' for more details.')


class UnsupportedForMessageFormatError(BrokerResponseError):
    errno = 43
    message = 'UNSUPPORTED_FOR_MESSAGE_FORMAT'
    description = ('The message format version on the broker does not'
                   ' support this request.')


class PolicyViolationError(BrokerResponseError):
    errno = 44
    message = 'POLICY_VIOLATION'
    description = 'Request parameters do not satisfy the configured policy.'


class SecurityDisabledError(BrokerResponseError):
    errno = 54
    message = 'SECURITY_DISABLED'
    description = 'Security features are disabled.'


class NonEmptyGroupError(BrokerResponseError):
    errno = 68
    message = 'NON_EMPTY_GROUP'
    description = 'The group is not empty.'


class GroupIdNotFoundError(BrokerResponseError):
    errno = 69
    message = 'GROUP_ID_NOT_FOUND'
    description = 'The group id does not exist.'


class KafkaUnavailableError(KafkaError):
    pass


class KafkaTimeoutError(KafkaError):
    pass


class FailedPayloadsError(KafkaError):
    def __init__(self, payload, *args):
        super(FailedPayloadsError, self).__init__(*args)
        self.payload = payload


class KafkaConnectionError(KafkaError):
    retriable = True
    invalid_metadata = True


class ProtocolError(KafkaError):
    pass


class UnsupportedCodecError(KafkaError):
    pass


class KafkaConfigurationError(KafkaError):
    pass


class QuotaViolationError(KafkaError):
    pass


class AsyncProducerQueueFull(KafkaError):
    def __init__(self, failed_msgs, *args):
        super(AsyncProducerQueueFull, self).__init__(*args)
        self.failed_msgs = failed_msgs


def _iter_broker_errors():
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and issubclass(obj, BrokerResponseError) and obj != BrokerResponseError:
            yield obj


kafka_errors = dict([(x.errno, x) for x in _iter_broker_errors()])


def for_code(error_code):
    return kafka_errors.get(error_code, UnknownError)


def check_error(response):
    if isinstance(response, Exception):
        raise response
    if response.error:
        error_class = kafka_errors.get(response.error, UnknownError)
        raise error_class(response)


RETRY_BACKOFF_ERROR_TYPES = (
    KafkaUnavailableError, LeaderNotAvailableError,
    KafkaConnectionError, FailedPayloadsError
)


RETRY_REFRESH_ERROR_TYPES = (
    NotLeaderForPartitionError, UnknownTopicOrPartitionError,
    LeaderNotAvailableError, KafkaConnectionError
)


RETRY_ERROR_TYPES = RETRY_BACKOFF_ERROR_TYPES + RETRY_REFRESH_ERROR_TYPES