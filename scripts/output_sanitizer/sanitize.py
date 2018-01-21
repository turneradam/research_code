from sys import argv
import json
import os

__doc__ = """
Name: Output Sanitizer for the F-7000 FL Spectrophotometer
Author: Tai Kersten
Email: kerstentw@gmail.com


This script creates json outputs and returns easily
Processible json or python dictionary objects
for later use.  

"""


# Default Constants
TARGET_FILE = "test_spectrum.txt"
target_data = open(TARGET_FILE,"r").read()
OUTPUT_FILE = False
VERBOSE = False

#ARGV filters



if len(argv) > 1:
    for flag in argv:
        if flag == "-i":
            file_index = argv.index("-i") + 1
            TARGET_FILE = argv[file_index]

        if flag == "-o":
            output_index = argv.index("-o") + 1
            OUTPUT_FILE = os.path.join("outputs",argv[output_index])

        if flag == "-v":
            VERBOSE = True
#Functions

def removeSpecials(_string):
    """
    Returns a processed String 
    that removes tabs and other escapes
    """

    specials = ["\n","\t","\r","\b"]
    
    for s in specials:
        _string = _string.replace(s,"")
    
    return _string


def createDict(entry):
    """
    Calls removeSpecials
    returns a single key:value pair 
    """

    if not entry:
        return

    elif entry.find(":") >= 0:
        entry_list = entry.split(":")     
        return {removeSpecials(entry_list[0]) : removeSpecials(entry_list[1])}

    elif entry[0].isdigit() == True:
        return tuple([float(i) for i in entry.split("\t")])

    else:
        return {"dump" : entry}

def create_output_dictionary():
    """
    Processes an output sheet.
    Returns a dictionary
    """
    
    master_dict = {"data":[]}
    data_list = target_data.split("\r\n")

    for entry in data_list:
        processed_entry = createDict(entry)

        if type(processed_entry) == dict:
            master_dict.update(processed_entry)

        elif type(processed_entry) == tuple:
            master_dict["data"].append(processed_entry)

    if OUTPUT_FILE:
        with open(OUTPUT_FILE,"w") as fil:
            fil.write(json.dumps(master_dict))
         

    return master_dict

if __name__ == "__main__":
    if VERBOSE:
        print create_output_dictionary()

