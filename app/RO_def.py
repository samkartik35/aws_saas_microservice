import sys
import socket
import argparse
import threading
import time
import select

from datetime import datetime
from pytz import timezone

import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import socket
import os
import datetime
REGION_CODE = "INDIA"

def initialiseRegionCode():
    pass

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

def InitialiseRegionCode(REGION_CODE):
    pass

def CreateInstanceIDForRO():
    pass
def InitialiseLocalVariables():
    pass
def InitialiseEnvironmentalVariables():
    pass
def InitialiseKafkaVars():
    pass
def RO_StandaloneInit():
	InitialiseRegionCode(REGION_CODE)
	CreateInstanceIDForRO()
	InitialiseLocalVariables()
	InitialiseKafkaVars()  # HostName
	InitialiseEnvironmentalVariables()
 
def createInstanceIDForRO(env_var):
    pass