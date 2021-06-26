# MongoDB coordinates
#	Hostname -  mongodb://NQ_US_DEV_IH9R15TP_GVIF8OOUNQ:DbPass123@ec2-52-86-101-212.compute-1.amazonaws.com:27017
#	DB Name - IH9R15TP_GVIF8OOUNQ
#	Username - NQ_US_DEV_IH9R15TP_GVIF8OOUNQ
#	Password - "DbPass123"
HOST_NAME_DATABASE = "mongodb://NQ_US_DEV_IH9R15TP_GVIF8OOUNQ:DbPass123@ec2-52-86-101-212.compute-1.amazonaws.com"
DATABSE_PORT = 27017
DATABASE_NAME = "IH9R15TP_GVIF8OOUNQ"
DATABASE_USER = "NQ_US_DEV_IH9R15TP_GVIF8OOUNQ"
DATABASE_PASSWORD = "DbPass123"

# MongoDB error codes definitions


MongoErrorCode = {
  OK = 0,
  INTERNAL_ERROR = 1,
  BAD_VALUE = 2,
  OBSOLETE_DUPLICATE_KEY = 3,
  NO_SUCH_KEY = 4,
  GRAPH_CONTAINS_CYCLE = 5,
  HOST_UNREACHABLE = 6,
  HOST_NOT_FOUND = 7,
  UNKNOWN_ERROR = 8,
  FAILED_TO_PARSE = 9,
  CANNOT_MUTATE_OBJECT = 10,
  USER_NOT_FOUND = 11,
  UNSUPPORTED_FORMAT = 12,
  UNAUTHORIZED = 13,
  TYPE_MISMATCH = 14,
  OVERFLOW = 15,
  INVALID_LENGTH = 16,
  PROTOCOL_ERROR = 17,
  AUTHENTICATION_FAILED = 18,
  CANNOT_REUSE_OBJECT = 19,
  ILLEGAL_OPERATION = 20,
  EMPTY_ARRAY_OPERATION = 21,
  INVALID_B_S_O_N = 22,
  ALREADY_INITIALIZED = 23,
  LOCK_TIMEOUT = 24,
  REMOTE_VALIDATION_ERROR = 25,
  NAMESPACE_NOT_FOUND = 26,
  INDEX_NOT_FOUND = 27,
  PATH_NOT_VIABLE = 28,
  NON_EXISTENT_PATH = 29,
  INVALID_PATH = 30,
  ROLE_NOT_FOUND = 31,
  ROLES_NOT_RELATED = 32,
  PRIVILEGE_NOT_FOUND = 33,
  CANNOT_BACKFILL_ARRAY = 34,
  USER_MODIFICATION_FAILED = 35,
  REMOTE_CHANGE_DETECTED = 36,
  FILE_RENAME_FAILED = 37,
  FILE_NOT_OPEN = 38,
  FILE_STREAM_FAILED = 39,
  CONFLICTING_UPDATE_OPERATORS = 40,
  FILE_ALREADY_OPEN = 41,
  LOG_WRITE_FAILED = 42,
  CURSOR_NOT_FOUND = 43,
  USER_DATA_INCONSISTENT = 45,
  LOCK_BUSY = 46,
  NO_MATCHING_DOCUMENT = 47,
  NAMESPACE_EXISTS = 48,
  INVALID_ROLE_MODIFICATION = 49,
  MAX_TIME_MS_EXPIRED = 50,
  MANUAL_INTERVENTION_REQUIRED = 51,
  DOLLAR_PREFIXED_FIELD_NAME = 52,
  INVALID_ID_FIELD = 53,
  NOT_SINGLE_VALUE_FIELD = 54,
  INVALID_D_B_REF = 55,
  EMPTY_FIELD_NAME = 56,
  DOTTED_FIELD_NAME = 57,
  ROLE_MODIFICATION_FAILED = 58,
  COMMAND_NOT_FOUND = 59,
  OBSOLETE_DATABASE_NOT_FOUND = 60,
  SHARD_KEY_NOT_FOUND = 61,
  OPLOG_OPERATION_UNSUPPORTED = 62,
  STALE_SHARD_VERSION = 63,
  WRITE_CONCERN_FAILED = 64,
  MULTIPLE_ERRORS_OCCURRED = 65,
  IMMUTABLE_FIELD = 66,
  CANNOT_CREATE_INDEX = 67,
  INDEX_ALREADY_EXISTS = 68,
  AUTH_SCHEMA_INCOMPATIBLE = 69,
  SHARD_NOT_FOUND = 70,
  REPLICA_SET_NOT_FOUND = 71,
  INVALID_OPTIONS = 72,
  INVALID_NAMESPACE = 73,
  NODE_NOT_FOUND = 74,
  WRITE_CONCERN_LEGACY_O_K = 75,
  NO_REPLICATION_ENABLED = 76,
  OPERATION_INCOMPLETE = 77,
  COMMAND_RESULT_SCHEMA_VIOLATION = 78,
  UNKNOWN_REPL_WRITE_CONCERN = 79,
  ROLE_DATA_INCONSISTENT = 80,
  NO_MATCH_PARSE_CONTEXT = 81,
  NO_PROGRESS_MADE = 82,
  REMOTE_RESULTS_UNAVAILABLE = 83,
  DUPLICATE_KEY_VALUE = 84,
  INDEX_OPTIONS_CONFLICT = 85,
  INDEX_KEY_SPECS_CONFLICT = 86,
  CANNOT_SPLIT = 87,
  SPLIT_FAILED_OBSOLETE = 88,
  NETWORK_TIMEOUT = 89,
  CALLBACK_CANCELED = 90,
  SHUTDOWN_IN_PROGRESS = 91,
  SECONDARY_AHEAD_OF_PRIMARY = 92,
  INVALID_REPLICA_SET_CONFIG = 93,
  NOT_YET_INITIALIZED = 94,
  NOT_SECONDARY = 95,
  OPERATION_FAILED = 96,
  NO_PROJECTION_FOUND = 97,
  DB_PATH_IN_USE = 98,
  UNSATISFIABLE_WRITE_CONCERN = 100,
  OUTDATED_CLIENT = 101,
  INCOMPATIBLE_AUDIT_METADATA = 102,
  NEW_REPLICA_SET_CONFIGURATION_INCOMPATIBLE = 103,
  NODE_NOT_ELECTABLE = 104,
  INCOMPATIBLE_SHARDING_METADATA = 105,
  DISTRIBUTED_CLOCK_SKEWED = 106,
  LOCK_FAILED = 107,
  INCONSISTENT_REPLICA_SET_NAMES = 108,
  CONFIGURATION_IN_PROGRESS = 109,
  CANNOT_INITIALIZE_NODE_WITH_DATA = 110,
  NOT_EXACT_VALUE_FIELD = 111,
  WRITE_CONFLICT = 112,
  INITIAL_SYNC_FAILURE = 113,
  INITIAL_SYNC_OPLOG_SOURCE_MISSING = 114,
  COMMAND_NOT_SUPPORTED = 115,
  DOC_TOO_LARGE_FOR_CAPPED = 116,
  CONFLICTING_OPERATION_IN_PROGRESS = 117,
  NAMESPACE_NOT_SHARDED = 118,
  INVALID_SYNC_SOURCE = 119,
  OPLOG_START_MISSING = 120,
  DOCUMENT_VALIDATION_FAILURE = 121,
  OBSOLETE_READ_AFTER_OPTIME_TIMEOUT = 122,
  NOT_A_REPLICA_SET = 123,
  INCOMPATIBLE_ELECTION_PROTOCOL = 124,
  COMMAND_FAILED = 125,
  RPC_PROTOCOL_NEGOTIATION_FAILED = 126,
  UNRECOVERABLE_ROLLBACK_ERROR = 127,
  LOCK_NOT_FOUND = 128,
  LOCK_STATE_CHANGE_FAILED = 129,
  SYMBOL_NOT_FOUND = 130,
  OBSOLETE_CONFIG_SERVERS_INCONSISTENT = 132,
  FAILED_TO_SATISFY_READ_PREFERENCE = 133,
  READ_CONCERN_MAJORITY_NOT_AVAILABLE_YET = 134,
  STALE_TERM = 135,
  CAPPED_POSITION_LOST = 136,
  INCOMPATIBLE_SHARDING_CONFIG_VERSION = 137,
  REMOTE_OPLOG_STALE = 138,
  JS_INTERPRETER_FAILURE = 139,
  INVALID_SSL_CONFIGURATION = 140,
  SSL_HANDSHAKE_FAILED = 141,
  JS_UNCATCHABLE_ERROR = 142,
  CURSOR_IN_USE = 143,
  INCOMPATIBLE_CATALOG_MANAGER = 144,
  POOLED_CONNECTIONS_DROPPED = 145,
  EXCEEDED_MEMORY_LIMIT = 146,
  Z_LIB_ERROR = 147,
  READ_CONCERN_MAJORITY_NOT_ENABLED = 148,
  NO_CONFIG_MASTER = 149,
  STALE_EPOCH = 150,
  OPERATION_CANNOT_BE_BATCHED = 151,
  OPLOG_OUT_OF_ORDER = 152,
  CHUNK_TOO_BIG = 153,
  INCONSISTENT_SHARD_IDENTITY = 154,
  CANNOT_APPLY_OPLOG_WHILE_PRIMARY = 155,
  OBSOLETE_NEEDS_DOCUMENT_MOVE = 156,
  CAN_REPAIR_TO_DOWNGRADE = 157,
  MUST_UPGRADE = 158,
  DURATION_OVERFLOW = 159,
  MAX_STALENESS_OUT_OF_RANGE = 160,
  INCOMPATIBLE_COLLATION_VERSION = 161,
  COLLECTION_IS_EMPTY = 162,
  ZONE_STILL_IN_USE = 163,
  INITIAL_SYNC_ACTIVE = 164,
  VIEW_DEPTH_LIMIT_EXCEEDED = 165,
  COMMAND_NOT_SUPPORTED_ON_VIEW = 166,
  OPTION_NOT_SUPPORTED_ON_VIEW = 167,
  INVALID_PIPELINE_OPERATOR = 168,
  COMMAND_ON_SHARDED_VIEW_NOT_SUPPORTED_ON_MONGOD = 169,
  TOO_MANY_MATCHING_DOCUMENTS = 170,
  CANNOT_INDEX_PARALLEL_ARRAYS = 171,
  TRANSPORT_SESSION_CLOSED = 172,
  TRANSPORT_SESSION_NOT_FOUND = 173,
  TRANSPORT_SESSION_UNKNOWN = 174,
  QUERY_PLAN_KILLED = 175,
  FILE_OPEN_FAILED = 176,
  ZONE_NOT_FOUND = 177,
  RANGE_OVERLAP_CONFLICT = 178,
  WINDOWS_PDH_ERROR = 179,
  BAD_PERF_COUNTER_PATH = 180,
  AMBIGUOUS_INDEX_KEY_PATTERN = 181,
  INVALID_VIEW_DEFINITION = 182,
  CLIENT_METADATA_MISSING_FIELD = 183,
  CLIENT_METADATA_APP_NAME_TOO_LARGE = 184,
  CLIENT_METADATA_DOCUMENT_TOO_LARGE = 185,
  CLIENT_METADATA_CANNOT_BE_MUTATED = 186,
  LINEARIZABLE_READ_CONCERN_ERROR = 187,
  INCOMPATIBLE_SERVER_VERSION = 188,
  PRIMARY_STEPPED_DOWN = 189,
  MASTER_SLAVE_CONNECTION_FAILURE = 190,
  OBSOLETE_BALANCER_LOST_DISTRIBUTED_LOCK = 191,
  FAIL_POINT_ENABLED = 192,
  NO_SHARDING_ENABLED = 193,
  BALANCER_INTERRUPTED = 194,
  VIEW_PIPELINE_MAX_SIZE_EXCEEDED = 195,
  INVALID_INDEX_SPECIFICATION_OPTION = 197,
  OBSOLETE_RECEIVED_OP_REPLY_MESSAGE = 198,
  REPLICA_SET_MONITOR_REMOVED = 199,
  CHUNK_RANGE_CLEANUP_PENDING = 200,
  CANNOT_BUILD_INDEX_KEYS = 201,
  NETWORK_INTERFACE_EXCEEDED_TIME_LIMIT = 202,
  SHARDING_STATE_NOT_INITIALIZED = 203,
  TIME_PROOF_MISMATCH = 204,
  CLUSTER_TIME_FAILS_RATE_LIMITER = 205,
  NO_SUCH_SESSION = 206,
  INVALID_UUID = 207,
  TOO_MANY_LOCKS = 208,
  STALE_CLUSTER_TIME = 209,
  CANNOT_VERIFY_AND_SIGN_LOGICAL_TIME = 210,
  KEY_NOT_FOUND = 211,
  INCOMPATIBLE_ROLLBACK_ALGORITHM = 212,
  DUPLICATE_SESSION = 213,
  AUTHENTICATION_RESTRICTION_UNMET = 214,
  DATABASE_DROP_PENDING = 215,
  ELECTION_IN_PROGRESS = 216,
  INCOMPLETE_TRANSACTION_HISTORY = 217,
  UPDATE_OPERATION_FAILED = 218,
  FTDC_PATH_NOT_SET = 219,
  FTDC_PATH_ALREADY_SET = 220,
  INDEX_MODIFIED = 221,
  CLOSE_CHANGE_STREAM = 222,
  ILLEGAL_OP_MSG_FLAG = 223,
  QUERY_FEATURE_NOT_ALLOWED = 224,
  TRANSACTION_TOO_OLD = 225,
  ATOMICITY_FAILURE = 226,
  CANNOT_IMPLICITLY_CREATE_COLLECTION = 227,
  SESSION_TRANSFER_INCOMPLETE = 228,
  MUST_DOWNGRADE = 229,
  D_N_S_HOST_NOT_FOUND = 230,
  D_N_S_PROTOCOL_ERROR = 231,
  MAX_SUB_PIPELINE_DEPTH_EXCEEDED = 232,
  TOO_MANY_DOCUMENT_SEQUENCES = 233,
  RETRY_CHANGE_STREAM = 234,
  INTERNAL_ERROR_NOT_SUPPORTED = 235,
  FOR_TESTING_ERROR_EXTRA_INFO = 236,
  CURSOR_KILLED = 237,
  NOT_IMPLEMENTED = 238,
  SNAPSHOT_TOO_OLD = 239,
  DNS_RECORD_TYPE_MISMATCH = 240,
  CONVERSION_FAILURE = 241,
  CANNOT_CREATE_COLLECTION = 242,
  INCOMPATIBLE_WITH_UPGRADED_SERVER = 243,
  NOT_YET_AVAILABLE_TRANSACTION_ABORTED = 244,
  BROKEN_PROMISE = 245,
  SNAPSHOT_UNAVAILABLE = 246,
  PRODUCER_CONSUMER_QUEUE_BATCH_TOO_LARGE = 247,
  PRODUCER_CONSUMER_QUEUE_END_CLOSED = 248,
  STALE_DB_VERSION = 249,
  STALE_CHUNK_HISTORY = 250,
  NO_SUCH_TRANSACTION = 251,
  REENTRANCY_NOT_ALLOWED = 252,
  FREE_MON_HTTP_IN_FLIGHT = 253,
  FREE_MON_HTTP_TEMPORARY_FAILURE = 254,
  FREE_MON_HTTP_PERMANENT_FAILURE = 255,
  TRANSACTION_COMMITTED = 256,
  TRANSACTION_TOO_LARGE = 257,
  UNKNOWN_FEATURE_COMPATIBILITY_VERSION = 258,
  KEYED_EXECUTOR_RETRY = 259,
  INVALID_RESUME_TOKEN = 260,
  TOO_MANY_LOGICAL_SESSIONS = 261,
  EXCEEDED_TIME_LIMIT = 262,
  OPERATION_NOT_SUPPORTED_IN_TRANSACTION = 263,
  TOO_MANY_FILES_OPEN = 264,
  ORPHANED_RANGE_CLEAN_UP_FAILED = 265,
  FAIL_POINT_SET_FAILED = 266,
  PREPARED_TRANSACTION_IN_PROGRESS = 267,
  CANNOT_BACKUP = 268,
  DATA_MODIFIED_BY_REPAIR = 269,
  REPAIRED_REPLICA_SET_NODE = 270,
  JS_INTERPRETER_FAILURE_WITH_STACK = 271,
  SOCKET_EXCEPTION = 9001,
  OBSOLETE_RECV_STALE_CONFIG = 9996,
  NOT_MASTER = 10107,
  CANNOT_GROW_DOCUMENT_IN_CAPPED_NAMESPACE = 10003,
  BSON_OBJECT_TOO_LARGE = 10334,
  DUPLICATE_KEY = 11000,
  INTERRUPTED_AT_SHUTDOWN = 11600,
  INTERRUPTED = 11601,
  INTERRUPTED_DUE_TO_STEP_DOWN = 11602,
  OUT_OF_DISK_SPACE = 14031,
  KEY_TOO_LONG = 17280,
  BACKGROUND_OPERATION_IN_PROGRESS_FOR_DATABASE = 12586,
  BACKGROUND_OPERATION_IN_PROGRESS_FOR_NAMESPACE = 12587,
  NOT_MASTER_OR_SECONDARY = 13436,
  NOT_MASTER_NO_SLAVE_OK = 13435,
  SHARD_KEY_TOO_BIG = 13334,
  STALE_CONFIG = 13388,
  DATABASE_DIFFER_CASE = 13297,
  OBSOLETE_PREPARE_CONFIGS_FAILED = 13104,
}

# Extra not including
# error_class not inserted

# BUG
# Some strings that have All Caps generated to have underscore after each letter
# Example DNS -> D_N_S

data = 'export enum MongoErrorCode {\n\t'

def convertChr(letter):
  if letter.isupper():
    return '_' + letter
  return letter.upper()


def convertStrToEnumName(name):
  newName = ''.join([convertChr(c) for c in name])
  if newName[0] == '_':
    newName = newName[1:]
  return newName


def createErrorEnum(name, code):
  return convertStrToEnumName(name) + ' = ' + str(code)


class ErrorCode:
  def __init__(self, name, code, extra = None):
    self.name = name
    self.code = code
    self.extra = extra
    global data
    data += self.__str__() + ',\n\t'

  def __str__(self):
    return createErrorEnum(self.name, self.code)


def error_code(name, code, extra = None):
  ErrorCode(name, code, extra)



def error_class(name, same):
  name += ''


def finish():
  global data
  data += '\n}'
  print data


error_code("OK", 0)
error_code("InternalError", 1)
error_code("BadValue", 2)
error_code("OBSOLETE_DuplicateKey", 3)
error_code("NoSuchKey", 4)
error_code("GraphContainsCycle", 5)
error_code("HostUnreachable", 6)
error_code("HostNotFound", 7)
error_code("UnknownError", 8)
error_code("FailedToParse", 9)
error_code("CannotMutateObject", 10)
error_code("UserNotFound", 11)
error_code("UnsupportedFormat", 12)
error_code("Unauthorized", 13)
error_code("TypeMismatch", 14)
error_code("Overflow", 15)
error_code("InvalidLength", 16)
error_code("ProtocolError", 17)
error_code("AuthenticationFailed", 18)
error_code("CannotReuseObject", 19)
error_code("IllegalOperation", 20)
error_code("EmptyArrayOperation", 21)
error_code("InvalidBSON", 22)
error_code("AlreadyInitialized", 23)
error_code("LockTimeout", 24)
error_code("RemoteValidationError", 25)
error_code("NamespaceNotFound", 26)
error_code("IndexNotFound", 27)
error_code("PathNotViable", 28)
error_code("NonExistentPath", 29)
error_code("InvalidPath", 30)
error_code("RoleNotFound", 31)
error_code("RolesNotRelated", 32)
error_code("PrivilegeNotFound", 33)
error_code("CannotBackfillArray", 34)
error_code("UserModificationFailed", 35)
error_code("RemoteChangeDetected", 36)
error_code("FileRenameFailed", 37)
error_code("FileNotOpen", 38)
error_code("FileStreamFailed", 39)
error_code("ConflictingUpdateOperators", 40)
error_code("FileAlreadyOpen", 41)
error_code("LogWriteFailed", 42)
error_code("CursorNotFound", 43)
error_code("UserDataInconsistent", 45)
error_code("LockBusy", 46)
error_code("NoMatchingDocument", 47)
error_code("NamespaceExists", 48)
error_code("InvalidRoleModification", 49)
error_code("MaxTimeMSExpired", 50)
error_code("ManualInterventionRequired", 51)
error_code("DollarPrefixedFieldName", 52)
error_code("InvalidIdField", 53)
error_code("NotSingleValueField", 54)
error_code("InvalidDBRef", 55)
error_code("EmptyFieldName", 56)
error_code("DottedFieldName", 57)
error_code("RoleModificationFailed", 58)
error_code("CommandNotFound", 59)
error_code("OBSOLETE_DatabaseNotFound", 60)
error_code("ShardKeyNotFound", 61)
error_code("OplogOperationUnsupported", 62)
error_code("StaleShardVersion", 63)
error_code("WriteConcernFailed", 64)
error_code("MultipleErrorsOccurred", 65)
error_code("ImmutableField", 66)
error_code("CannotCreateIndex", 67 )
error_code("IndexAlreadyExists", 68 )
error_code("AuthSchemaIncompatible", 69)
error_code("ShardNotFound", 70)
error_code("ReplicaSetNotFound", 71)
error_code("InvalidOptions", 72)
error_code("InvalidNamespace", 73)
error_code("NodeNotFound", 74)
error_code("WriteConcernLegacyOK", 75)
error_code("NoReplicationEnabled", 76)
error_code("OperationIncomplete", 77)
error_code("CommandResultSchemaViolation", 78)
error_code("UnknownReplWriteConcern", 79)
error_code("RoleDataInconsistent", 80)
error_code("NoMatchParseContext", 81)
error_code("NoProgressMade", 82)
error_code("RemoteResultsUnavailable", 83)
error_code("DuplicateKeyValue", 84)
error_code("IndexOptionsConflict", 85 )
error_code("IndexKeySpecsConflict", 86 )
error_code("CannotSplit", 87)
error_code("SplitFailed_OBSOLETE", 88)
error_code("NetworkTimeout", 89)
error_code("CallbackCanceled", 90)
error_code("ShutdownInProgress", 91)
error_code("SecondaryAheadOfPrimary", 92)
error_code("InvalidReplicaSetConfig", 93)
error_code("NotYetInitialized", 94)
error_code("NotSecondary", 95)
error_code("OperationFailed", 96)
error_code("NoProjectionFound", 97)
error_code("DBPathInUse", 98)
error_code("UnsatisfiableWriteConcern", 100)
error_code("OutdatedClient", 101)
error_code("IncompatibleAuditMetadata", 102)
error_code("NewReplicaSetConfigurationIncompatible", 103)
error_code("NodeNotElectable", 104)
error_code("IncompatibleShardingMetadata", 105)
error_code("DistributedClockSkewed", 106)
error_code("LockFailed", 107)
error_code("InconsistentReplicaSetNames", 108)
error_code("ConfigurationInProgress", 109)
error_code("CannotInitializeNodeWithData", 110)
error_code("NotExactValueField", 111)
error_code("WriteConflict", 112)
error_code("InitialSyncFailure", 113)
error_code("InitialSyncOplogSourceMissing", 114)
error_code("CommandNotSupported", 115)
error_code("DocTooLargeForCapped", 116)
error_code("ConflictingOperationInProgress", 117)
error_code("NamespaceNotSharded", 118)
error_code("InvalidSyncSource", 119)
error_code("OplogStartMissing", 120)
error_code("DocumentValidationFailure", 121) # Only for the document validator on collections.
error_code("OBSOLETE_ReadAfterOptimeTimeout", 122)
error_code("NotAReplicaSet", 123)
error_code("IncompatibleElectionProtocol", 124)
error_code("CommandFailed", 125)
error_code("RPCProtocolNegotiationFailed", 126)
error_code("UnrecoverableRollbackError", 127)
error_code("LockNotFound", 128)
error_code("LockStateChangeFailed", 129)
error_code("SymbolNotFound", 130)
#error_code("RLPInitializationFailed", 131) # Removed in 4.2
error_code("OBSOLETE_ConfigServersInconsistent", 132)
error_code("FailedToSatisfyReadPreference", 133)
error_code("ReadConcernMajorityNotAvailableYet", 134)
error_code("StaleTerm", 135)
error_code("CappedPositionLost", 136)
error_code("IncompatibleShardingConfigVersion", 137)
error_code("RemoteOplogStale", 138)
error_code("JSInterpreterFailure", 139)
error_code("InvalidSSLConfiguration", 140)
error_code("SSLHandshakeFailed", 141)
error_code("JSUncatchableError", 142)
error_code("CursorInUse", 143)
error_code("IncompatibleCatalogManager", 144)
error_code("PooledConnectionsDropped", 145)
error_code("ExceededMemoryLimit", 146)
error_code("ZLibError", 147)
error_code("ReadConcernMajorityNotEnabled", 148)
error_code("NoConfigMaster", 149)
error_code("StaleEpoch", 150)
error_code("OperationCannotBeBatched", 151)
error_code("OplogOutOfOrder", 152)
error_code("ChunkTooBig", 153)
error_code("InconsistentShardIdentity", 154)
error_code("CannotApplyOplogWhilePrimary", 155)
error_code("OBSOLETE_NeedsDocumentMove", 156)
error_code("CanRepairToDowngrade", 157)
error_code("MustUpgrade", 158)
error_code("DurationOverflow", 159)
error_code("MaxStalenessOutOfRange", 160)
error_code("IncompatibleCollationVersion", 161)
error_code("CollectionIsEmpty", 162)
error_code("ZoneStillInUse", 163)
error_code("InitialSyncActive", 164)
error_code("ViewDepthLimitExceeded", 165)
error_code("CommandNotSupportedOnView", 166)
error_code("OptionNotSupportedOnView", 167)
error_code("InvalidPipelineOperator", 168)
error_code("CommandOnShardedViewNotSupportedOnMongod", 169, extra='ResolvedView')
error_code("TooManyMatchingDocuments", 170)
error_code("CannotIndexParallelArrays", 171)
error_code("TransportSessionClosed", 172)
error_code("TransportSessionNotFound", 173)
error_code("TransportSessionUnknown", 174)
error_code("QueryPlanKilled", 175)
error_code("FileOpenFailed", 176)
error_code("ZoneNotFound", 177)
error_code("RangeOverlapConflict", 178)
error_code("WindowsPdhError", 179)
error_code("BadPerfCounterPath", 180)
error_code("AmbiguousIndexKeyPattern", 181)
error_code("InvalidViewDefinition", 182);
error_code("ClientMetadataMissingField", 183)
error_code("ClientMetadataAppNameTooLarge", 184)
error_code("ClientMetadataDocumentTooLarge", 185)
error_code("ClientMetadataCannotBeMutated", 186)
error_code("LinearizableReadConcernError", 187)
error_code("IncompatibleServerVersion", 188)
error_code("PrimarySteppedDown", 189)
error_code("MasterSlaveConnectionFailure", 190)
error_code("OBSOLETE_BalancerLostDistributedLock", 191)
error_code("FailPointEnabled", 192)
error_code("NoShardingEnabled", 193)
error_code("BalancerInterrupted", 194)
error_code("ViewPipelineMaxSizeExceeded", 195)
error_code("InvalidIndexSpecificationOption", 197)
error_code("OBSOLETE_ReceivedOpReplyMessage", 198)
error_code("ReplicaSetMonitorRemoved", 199)
error_code("ChunkRangeCleanupPending", 200)
error_code("CannotBuildIndexKeys", 201)
error_code("NetworkInterfaceExceededTimeLimit", 202)
error_code("ShardingStateNotInitialized", 203)
error_code("TimeProofMismatch", 204)
error_code("ClusterTimeFailsRateLimiter", 205)
error_code("NoSuchSession", 206)
error_code("InvalidUUID", 207)
error_code("TooManyLocks", 208)
error_code("StaleClusterTime", 209)
error_code("CannotVerifyAndSignLogicalTime", 210)
error_code("KeyNotFound", 211)
error_code("IncompatibleRollbackAlgorithm", 212)
error_code("DuplicateSession", 213)
error_code("AuthenticationRestrictionUnmet", 214)
error_code("DatabaseDropPending", 215)
error_code("ElectionInProgress", 216)
error_code("IncompleteTransactionHistory", 217);
error_code("UpdateOperationFailed", 218)
error_code("FTDCPathNotSet", 219)
error_code("FTDCPathAlreadySet", 220)
error_code("IndexModified", 221)
error_code("CloseChangeStream", 222)
error_code("IllegalOpMsgFlag", 223)
error_code("QueryFeatureNotAllowed", 224)
error_code("TransactionTooOld", 225)
error_code("AtomicityFailure", 226)
error_code("CannotImplicitlyCreateCollection", 227, extra="CannotImplicitlyCreateCollectionInfo");
error_code("SessionTransferIncomplete", 228)
error_code("MustDowngrade", 229)
error_code("DNSHostNotFound", 230)
error_code("DNSProtocolError", 231)
error_code("MaxSubPipelineDepthExceeded", 232)
error_code("TooManyDocumentSequences", 233)
error_code("RetryChangeStream", 234)
error_code("InternalErrorNotSupported", 235) # this function or module is not available on this platform or configuration
error_code("ForTestingErrorExtraInfo", 236, extra="ErrorExtraInfoExample")
error_code("CursorKilled", 237)
error_code("NotImplemented", 238)
error_code("SnapshotTooOld", 239)
error_code("DNSRecordTypeMismatch", 240)
error_code("ConversionFailure", 241)
error_code("CannotCreateCollection", 242)
error_code("IncompatibleWithUpgradedServer", 243)
error_code("NOT_YET_AVAILABLE_TransactionAborted", 244)
error_code("BrokenPromise", 245)
error_code("SnapshotUnavailable", 246)
error_code("ProducerConsumerQueueBatchTooLarge", 247)
error_code("ProducerConsumerQueueEndClosed", 248)
error_code("StaleDbVersion", 249, extra="StaleDbRoutingVersion")
error_code("StaleChunkHistory", 250)
error_code("NoSuchTransaction", 251)
error_code("ReentrancyNotAllowed", 252)
error_code("FreeMonHttpInFlight", 253)
error_code("FreeMonHttpTemporaryFailure", 254)
error_code("FreeMonHttpPermanentFailure", 255)
error_code("TransactionCommitted", 256)
error_code("TransactionTooLarge", 257)
error_code("UnknownFeatureCompatibilityVersion", 258);
error_code("KeyedExecutorRetry", 259);
error_code("InvalidResumeToken", 260);
error_code("TooManyLogicalSessions", 261);
error_code("ExceededTimeLimit", 262);
error_code("OperationNotSupportedInTransaction", 263);
error_code("TooManyFilesOpen", 264);
error_code("OrphanedRangeCleanUpFailed", 265);
error_code("FailPointSetFailed", 266);
error_code("PreparedTransactionInProgress", 267);
error_code("CannotBackup", 268);
error_code("DataModifiedByRepair", 269);
error_code("RepairedReplicaSetNode", 270);
error_code("JSInterpreterFailureWithStack", 271, extra="JSExceptionInfo")
# Error codes 4000-8999 are reserved.

# Non-sequential error codes (for compatibility only)
error_code("SocketException", 9001)
error_code("OBSOLETE_RecvStaleConfig", 9996)
error_code("NotMaster", 10107)
error_code("CannotGrowDocumentInCappedNamespace", 10003)
error_code("BSONObjectTooLarge", 10334)
error_code("DuplicateKey", 11000)
error_code("InterruptedAtShutdown", 11600)
error_code("Interrupted", 11601)
error_code("InterruptedDueToStepDown", 11602)
error_code("OutOfDiskSpace", 14031 )
# TODO SERVER-36385: Mark KeyTooLong error as obsolete
error_code("KeyTooLong", 17280);
error_code("BackgroundOperationInProgressForDatabase", 12586);
error_code("BackgroundOperationInProgressForNamespace", 12587);
error_code("NotMasterOrSecondary", 13436);
error_code("NotMasterNoSlaveOk", 13435);
error_code("ShardKeyTooBig", 13334);
error_code("StaleConfig", 13388, extra="StaleConfigInfo");
error_code("DatabaseDifferCase", 13297);
error_code("OBSOLETE_PrepareConfigsFailed", 13104);

# Group related errors into classes, can be checked against ErrorCodes::isXXXClassName methods.
error_class("NetworkError", ["HostUnreachable", "HostNotFound", "NetworkTimeout", "SocketException"])
error_class("Interruption", ["Interrupted",
                             "InterruptedAtShutdown",
                             "InterruptedDueToStepDown",
                             "ExceededTimeLimit",
                             "MaxTimeMSExpired",
                             "CursorKilled",
                             "LockTimeout"])

# isNotMasterError() includes all codes that indicate that the node that received the request was
# not master at some point during command processing, regardless of whether some write may have
# happened. If you care about whether a write could have happened, check for individual codes.
error_class("NotMasterError", [
  "NotMaster",
  "NotMasterNoSlaveOk",
  "NotMasterOrSecondary",
  "InterruptedDueToStepDown",
  "PrimarySteppedDown",
])
error_class("StaleShardVersionError",
            ["StaleConfig", "StaleShardVersion", "StaleEpoch"])
error_class("NeedRetargettingError",
            ["StaleConfig", "StaleShardVersion", "StaleEpoch", "CannotImplicitlyCreateCollection"])
error_class("WriteConcernError", ["WriteConcernFailed",
                                  "WriteConcernLegacyOK",
                                  "UnknownReplWriteConcern",
                                  "UnsatisfiableWriteConcern"])
error_class("ShutdownError", ["ShutdownInProgress", "InterruptedAtShutdown"])

#TODO SERVER-28679 add checksum failure.
error_class("ConnectionFatalMessageParseError", ["IllegalOpMsgFlag",
                                                 "TooManyDocumentSequences"])

error_class("ExceededTimeLimitError", ["ExceededTimeLimit", "MaxTimeMSExpired", "NetworkInterfaceExceededTimeLimit"])

error_class("SnapshotError", ["SnapshotTooOld", "SnapshotUnavailable", "StaleChunkHistory"])


finish()