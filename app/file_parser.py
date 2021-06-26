import os
import csv
import re # importing regex module for string procesing
# Config file format
# Service ID
   # Item -> Name Prefix count, Item Name, Item Type, Make, Model, Batch no, size, installation date
   #
   # Location -> Site ID, Site Name, Address1, Address2, zipcode, operating country, lat-long
   #
   # Gateway -> Gateway Name, Make, Model
   #         gwMCKHNIKHNIB001, Jinan USR IOT Technology Ltd.,USR-G786,
   # Gateway Connectivity -> Cloud connectivity, number of paths, Auth string SNMP Get, Auth String SNMP Trap
   #                         4g jio, 1, "",""
   # Sensor -> Sensor number, Sensor type, Param name, Make, Model, Operating range(min), Operating Range(max),Freq data collection
   #          1             ,
   #          Debounce logic, sensor redundancy, data attribute, synchronous group, component number, component name, sub-component number, sub-component name,
   # 
   #          Part number, Part name, Sensor locn,
   #
   # Space -> Space name, Space tpe, Struct type, Desc, SiteID, Site Name, Address1, Address2, zip,country,lat-long
   # 

ServiceID_Data ={
    "Item":{
        "Name Prefix count":"",
        "Item Name":"",
        "Item Type":"",
        "Make":"",
        "Model":"",
        "Batch no":"",
        "size":"",
        "installation date":""
        } ,
    "Location":{
        "Site ID":"",
        "Site Name":"",
        "Address1":"",
        "Address2":"",
        "zipcode":"",
        "operating country":"",
        "lat-long":""     
    },
    "Gateways":{
        "Gateway Name":"",
        "Make":"",
        "Model":"",
        },
    "Gateway Connectivity":{
        "Cloud connectivity":"",
        "number of paths":"",
        "Auth string SNMP Get":"",
        "Auth String SNMP Trap":""     
    },
    "Sensors":{
        "Sensor number":None,
        "Sensor type":"",
        "Param name":"",
        "Make":"",
        "Model":"",
        "Operating range(min)":"",
        "Operating Range(max)":"",
        "Freq data collection":"",
        "Debounce logic":"",
        "sensor redundancy":"",
        "data attribute":"",
        "synchronous group":"",
        "component number":"",
        "component name":"",
        "sub-component number":"",
        "sub-component name":"",
        "Part number":"",
        "Part name":"",
        "Sensor locn":""     
    },
    "Space":{
        "Space name":"",
        "Space type":"",
        "Struct type":"",
        "Desc, SiteID":"",
        "Site Name, Address1":"",
        "Address2":"",
        "zip":"",
        "country":"",
        "lat-long":""       
    }
    
}
  
# Config File for Network of Items
#Item ->
    # S No.,Customer Name,Customer No.,Operating Country,Item Id ,Description,Item Type,Make,Model,Batch No.,Size,Installation Date,
    # Image,Icon,Variable 1,Variable 2,Variable 3,Component No.,Description,Sub Component No.,Description,
# Location -> 
# State,# City,Zip/Pincode,Address 1,Address 2,Lat/Long,
# Config Groups ->
    # Groups,
# Gateway->
    # Resource Id,Gateway Description,Make ,Model,Installation Date,
    # Batch No.,Power Supply,Battery Capacity,No. of Sensors supported,OS & Version,Greengrass supported,SNMP Supported,
    # ECC supported (Edge),ECC supported (Cloud),CPU speed,Memory Capacity,
# Gateway Connectivity ->
    # Cloud Connectivity,Cloud Connectivity type,Cloud Connectivity Protocol,IP Address,Port No.,Subnet Mask,
    # Ingress Port no.,No. of Max Ports towards Sensors,Heartbeat Time,Heartbeat Rate,Heartbeat Data,
# SNMP ->
    # SNMP Protocol Version,Authentication Level,Authentication Method,Encryption,SNMP Port No.,
# Sensors ->
    # Sensor No.,Sensor Location Description,Resource Id,Make ,Model,Batch No.,Measuring Range (Min),
    # Measuring Range (Max),MTBF,Sensor type,Output Signal type,Output Data type,Interface,Power Source,Battery Capacity,
    # Gateway Connectivity type,Gateway Connectivity Protocol,Sensor Redundancy,Sensor lead,Synchronous ,Certificate
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Network_Of_Items = {
    "Item" : {
        "Sr. No":"",
        "Customer Name":"",
        "Operating Country":"",
        "Item ID":"",
        "Description":"",
        "Item Type":"",
        "Make":"",
        "Model":"",
        "Batch No.":"",
        "Size":"",
        "Installation Date":"",
        "Image":"",
        "Icon,Variable 1":"",
        "Variable 2":"",
        "Variable 3":"",
        "Component No.":"",
        "Description":"",
        "Sub Component No.":"",
        "Description":""
    },
    "Location":{
        "State":"",
        "City":"",
        "Zip/Pincode":"",
        "Address 1":"",
        "Address 2":"",
        "Lat/Long":""
    },
    "Config Groups":"Groups",
    "Gateway": {
        "Resource Id":"",
        "Gateway Description":"",
        "Make":"" ,
        "Model":"",
        "Installation Date":"",
        "Batch No.":"",
        "Power Supply":"",
        "Battery Capacity":"",
        "No. of Sensors supported":"",
        "OS & Version":"",
        "Greengrass supported":"",
        "SNMP Supported":"",
        "ECC supported (Edge)":"",
        "ECC supported (Cloud)":"",
        "CPU speed,Memory":"" ,
        "Capacity":""
    },
    "Gateway Connectivity"  :{
        "Cloud Connectivity":"",
        "Cloud Connectivity type":"",
        "Cloud Connectivity Protocol":"",
        "IP Address":"",
        "Port No.":"",
        "Subnet Mask":"",
        "Ingress Port no.":"",
        "No. of Max Ports":"", 
        "towards Sensors":"",
        "Heartbeat Time":"",
        "Heartbeat Rate":"",
        "Heartbeat Data":""
    },
    "SNMP":{
        "SNMP Protocol Version":"",
        "Authentication Level":"",
        "Authentication Method":"",
        "Encryption":"",
        "SNMP Port No.":""
    },
    "Sensors":{
        "Sensor No.":"",
        "Sensor Location Description":"" ,
        "Resource Id":"",
        "Make":"" ,
        "Model":"",
        "Batch No.":"",
        "Measuring":"" ,
        "Range (Min)":"",
        "Measuring Range (Max)":"",
        "MTBF,Sensor type":"",
        "Output Signal type":"",
        "Output Data type":"",
        "Interface":"",
        "Power Source":"",
        "Battery Capacity":"",
        "Gateway Connectivity type":"",
        "Gateway Connectivity Protocol":"",
        "Sensor Redundancy":"",
        "Sensor lead":"",
        "Synchronous":"" ,
        "Certificate":""
    },   
}

sensor_data ={
        "Resource Id":"",
        "Sensor number":None,
        "Sensor type":"",
        "Param name":"",
        "Make":"",
        "Model":"",
        "Operating range(min)":"",
        "Operating Range(max)":"",
        "Freq data collection":"",
        "Debounce logic":"",
        "sensor redundancy":"",
        "data attribute":"",
        "synchronous group":"",
        "component number":"",
        "component name":"",
        "sub-component number":"",
        "sub-component name":"",
        "Part number":"",
        "Part name":"",
        "Sensor locn":"",     
        "state":"",
        "prev-state":"",
        "current-event":"",
        "prev-event":"",
        "work-order raised":"",
        "sample count":None,
        "Idle time":"",
        
        }


gateway_data ={
       "Gateway": {
        "Resource Id":"",
        "Gateway Description":"",
        "Make":"" ,
        "Model":"",
        "Installation Date":"",
        "Batch No.":"",
        "Power Supply":"",
        "Battery Capacity":"",
        "No. of Sensors supported":"",
        "OS & Version":"",
        "Greengrass supported":"",
        "SNMP Supported":"",
        "ECC supported (Edge)":"",
        "ECC supported (Cloud)":"",
        "CPU speed,Memory":"" ,
        "Capacity":""
    },
    "Gateway Connectivity"  :{
        "Cloud Connectivity":"",
        "Cloud Connectivity type":"",
        "Cloud Connectivity Protocol":"",
        "IP Address":"",
        "Port No.":"",
        "Subnet Mask":"",
        "Ingress Port no.":"",
        "No. of Max Ports":"", 
        "towards Sensors":"",
        "Heartbeat Time":"",
        "Heartbeat Rate":"",
        "Heartbeat Data":""
    },
    "SNMP":{
        "SNMP Protocol Version":"",
        "Authentication Level":"",
        "Authentication Method":"",
        "Encryption":"",
        "SNMP Port No.":""
    },
}

idleDeviceTable[] = {
    "Device ID":"",
    "Time Stamp":""
}

PhysicalThingCommStsTable[] ={
    "Thing Name":"",
    "No of sensors":"",
    ""
}

class Gateway:
    def__init__(self,data,Sensors_data):
        self.Data = data 
        self.Sensors = []
    def add_sensors(self,sensor_data):
        self.Sensors.append(sensor_data)
        
# Run Operation Data structure for serviceID
class ServiceID:
    """ Service ID class"""
    def __init__(self, serviceid):
        self.serviceID = serviceid
        self.Gateway = []
        
# Function to change time to IST
# eg. "2020-10-07 13:18:23"
def get_time_stamp():
    fmt = "%Y-%m-%d %H:%M:%S"

    now_time = datetime.now(timezone('ASIA/Calcutta'))
    time = now_time.strftime(fmt)
    return(time)

  
# function to return topic and no of sensors from a file when siteid and config file name is passed.
def parse_config_file(config_file, debug):
    
    env_var = {}
    with open(config_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                if(debug == True):
                    print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if(debug == True):
                    print("Here is row")
                    print(row)
                if(siteid == row[0]):
                    if(debug == True):
                        print("Line count:",line_count)
                    topicid_list.append(row[2] + '/' + row[3] + '/' + row[4]+'/'+ row[5] + '/' + row[6] + '/' + row[7])
                    numberOfSensors = row[1]
                    param_list.append(row[7]) #Create list of parameters
                line_count += 1
            if(debug == True):
                print("topic list, param list and no of sensors:")
                print(topicid_list,param_list, numberOfSensors)
    return(topicid_list,param_list,numberOfSensors)

