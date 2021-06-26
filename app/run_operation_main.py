''' Main file for the Run Operation. There is one instance of Run Operation per Service ID'''
from kafka import KafkaConsumer
from multiprocessing import Process, Queue 
import time
from gateway_state_def import *
from json import loads
from RO_def import *
from file_parser import *




	
	

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
    
    print("Number of Arguments:",len(sys.argv),"arguments.")
    print("Argument list:",str(sys.argv))

    parser = argparse.ArgumentParser(description = "This is the server for the multithreaded socket demo!")
    parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = "")
    parser.add_argument('--boot_type', metavar = 'boot_type', type = str, nargs = '?', default = "CREATE_INITIAL")
    parser.add_argument('--config', metavar = 'configfile', type = str, nargs = '?', default = "RO_config.txt")
    parser.add_argument('--debug', metavar = 'debug', type = bool, nargs = '?', default = False)
    args = parser.parse_args()
    boot_type = args.boot_type()
    config_file = args.configfile()
    debug = args.debug()
    env_var = {}
    env_var = parse_config_file(config_file, debug)
    

	# nextqore admin starts the RO micro-service with –boot_type = CREATE_INITIAL, --region_code and config file
 	# INDIA. Both these variables are stored as part of environment variables.
	# nextqore admin also specifies kafka and mongodb endpoint while starting the micro-service.
    initialiseRegionCode(env_var["region code"])
    instanceID = createInstanceIDForRO(env_var["instance"])

	# Initialise variables related to mongodb and kafka interfaces.
	initialiseLocalVariables():
	initialiseKafkaVars()  
	initialiseMongoDBVars()

	RO_StandaloneInit()
	RO_InterfaceInit()
 
	q = Queue()
	p1 = Process(target = RO_mainLoop, args=("Customer1",5,))
	p1.start()
	p2 = Process(target = RO_mainLoop, args=("Customer2",5,))
	p2.start()
	while 1:
		print("main process")
		time.sleep(10)
	



