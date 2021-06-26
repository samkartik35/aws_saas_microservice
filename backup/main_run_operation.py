''' Main file for the Run Operation. There is one instance of Run Operation per Service ID'''
from kafka import KafkaConsumer
from multiprocessing import Process, Queue 
import time
from gateway_state_def import *
from json import loads

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
''' Consumer for data topics'''
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

''' Read configuraration from file '''
def readMasterConfiguration():
	pass

def initECCConfiguration():
	pass
def sendECCConfiguration():
	pass

''' Initialise User Interfaces '''
def initaliseUserInterfaces():
	pass

''' Initialise Configurations '''
def initConfigurations():
	pass

''' Initialise Timers '''
def initTimers():
	pass

''' Process Parameter Change request received from UI, we can receive a file or individual parameters.'''
def processParameterChangeRequest(parameters):
	''' Check if parameter passed a file or a list and then do change management 
	as per parameters'''
	pass

''' apply parameter changes to db '''
def applyParameterChange():
	pass
def initRESTInterface():
	pass
def initRESTInterface():
	pass
def initMongoDB():
	pass
def initKafka():
	pass
def initConfiguration():
    pass	
def RO_startupRoutine():
	initConfiguration()
	initTimers()
	initECCConfiguration()
	initRESTInterface()
	initMongoDB()
	
	

def RO_mainLoop(threadName, delay):
	print(threadName)
	name = "Process executing" + threadName
	while True:
		print(name)
		time.sleep(10)
	

''' Create and Initialise Network , Gateways and Sensor Objects '''

''' Run Operation Main loop '''
''' Start infinite loop waiting for events from Kafka queue.If event received'''
if __name__ == "__main__":
	RO_startupRoutine()
	q = Queue()
	p1 = Process(target = RO_mainLoop, args=("Customer1",5,))
	p1.start()
	p2 = Process(target = RO_mainLoop, args=("Customer2",5,))
	p2.start()
	while 1:
		print("main process")
		time.sleep(10)
	



