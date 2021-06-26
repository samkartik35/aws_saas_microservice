''' Main file for the Run Operation. There is one process runs per Service ID'''
from RO_init import *
	
def RO_startupRoutine():
	
	RO_initConfiguration() # Initialise Customer device tree and its parameters.
	
	RO_initTimers()
	
	RO_initRESTInterface()
	
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
	



