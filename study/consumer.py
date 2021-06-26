''' File: consumer.py '''
from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
from kafka_def import *
import threading
import time
'''
The first argument is the topic, KAFKA_DATA_TOPIC in our case.
bootstrap_servers=[KAFKA_SERVER]: same as our producer
auto_offset_reset=’earliest’: one of the most important arguments. 
It handles where the consumer restarts reading after breaking down or 
being turned off and can be set either to earliest or latest. When set 
to latest, the consumer starts reading at the end of the log. When set 
to earliest, the consumer starts reading at the latest committed offset. 
And that’s exactly what we want here.
enable_auto_commit=True: makes sure the consumer commits its read 
offset every interval.
auto_commit_interval_ms=1000ms: sets the interval between two commits. 
Since messages are coming in every five second, committing every second 
seems fair.
group_id=’counters’: this is the consumer group to which the consumer 
belongs. Remember from the introduction that a consumer needs to be part 
of a consumer group to make the auto commit work.
The value deserializer deserializes the data into a common json format,
 the inverse of what our value serializer was doing
'''
''' KAFKA data queue '''

def processDataQueue():
     time.sleep(1)
     consumer_data = KafkaConsumer(
     KAFKA_DATA_TOPIC,
     bootstrap_servers=[KAFKA_SERVER],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
     
     for message in consumer_data: 	 	
         message = message.value
         '''collection.insert_one(message)
         print('{} added to {}'.format(message, collection))'''
         print("Data message:",message)

   
     

''' KAFKA Control queue '''

def procesControlQueue():
     time.sleep(1)
     consumer_control = KafkaConsumer(
     KAFKA_CONTROL_TOPIC,
     bootstrap_servers=[KAFKA_SERVER],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
     
     for message in consumer_control:
         message = message.value
         '''collection.insert_one(message)
         print('{} added to {}'.format(message, collection))'''
         print("Control messag:",message)


# Create two threads as follows
try:
     ''' Creating the thread to process control queue'''
     thread1 = threading.Thread(target = procesControlQueue, args = ())
     time.sleep(1)   
     
     ''' Creating the thread to process control queue'''
     thread2 = threading.Thread(target = processDataQueue, args = ())   
     time.sleep(1)
     ''' Starting the thread to process control queue'''
     thread1.start()
     time.sleep(1)
     ''' Starting the thread to process control queue'''
     thread2.start()
except:
   print ("Error: unable to start thread")
