from kafka import KafkaConsumer
from multiprocessing import Process, Queue 
import time
from gateway_state_def import *
from json import loads
from pymongo import MongoClient

# Docker image shall include mongoDB image. A mongoDB daemon in installed(
# sudo apt install mongodb), enabled(sudo systemctl enable mongodb) and started(sudo systemctl start mongodb)

def initMongoDB():
	client = MongoClient(port=MONGODB_CLIENT_PORT)
	db=client.business

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
	
def initKafka():
	pass
def initConfiguration():
    pass
