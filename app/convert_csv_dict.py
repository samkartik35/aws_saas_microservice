#!/usr/bin/env python
 
import csv
import sys
import pprint
 
# Function to convert a csv file to a list of dictionaries.  Takes in one variable called &quot;variables_file&quot;
 
def csv_dict_list(variables_file):
     
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
 
    reader = csv.DictReader(open(variables_file, 'rb'))
    dict_list = []
    
    for line in reader:
        dict_list.append(line)
        print(line)
    return dict_list
 
# Calls the csv_dict_list function, passing the named csv
 
device_values = csv_dict_list(sys.argv[1])
 
# Prints the results nice and pretty like
 
pprint.pprint(device_values)