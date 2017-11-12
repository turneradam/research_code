
import json
import config

class DataWrapper(object):

    def __processKeys(self):
        for _string in self.splitOnNL:
        	if _string.endswith(":"):
                self.__setattr__(_string,self.splitOnNL[self.splitOnNL.indexOf(_string) + 1])
            
            else: 
                pass

    def __processIntegerList(self):
    	"""Create Data Pairs"""

        for _string in self.splitOnNL:
        	pass

    def __repr__(self):
    	return self.fileName

    def __init__(self,_fileName):
    	try:
            with open(_fileName,"r") as fil:
        	    self.rawString = fil.read()
            self.fileName = _fileName

        except:
        	print("Invalid Filename, skipping")
        	pass

        self.splitOnNL = self.rawString.split("\n")
        __processKeys()




class SpecJSON(object):
    def __init__(self):
    	data_sets = []
        for fil in config.parseFiles:
        	data_sets.append(DataWrapper(fil))


