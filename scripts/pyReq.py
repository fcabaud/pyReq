#!/usr/bin/python
# Goal: Requirement management stored in a Json file
import json
from collections import OrderedDict
import os

# A requirement is a dictionnary composed of:

C_KEY_TAG          = "tag"           # unique key for getting the requirement
C_KEY_DOCUMENT     = "document"      # file document name (pdf, doc, xls,...) docExample.pdf is in path ../in
C_KEY_BODY         = "body"          # simple (and clear) sentence contaning the requiment
C_KEY_COVERAGE     = "coverage"      # list of othre requirements covered by requirement "tag"
C_KEY_ATTRIBUTES   = "attribute"     # open list of attributes (example of attributes: Sprint : sprint when the tag is planned to be developped)

C_PATH_IN          = os.pardir+os.sep+'in'+os.sep    # path where input doc are (docExample.pdf can be here)
C_PATH_OUT         = os.pardir+os.sep+'out'+os.sep   # path where ouput doc are (coverage.xlsx can be generated here)
C_PATH_WORK        = os.pardir+os.sep+"work"+os.sep  # path where json files are

class error(BaseException):
  """ class for Error management for pyReq 
        but also for inheritance classes
  """
  def __init__(self, data):
    self.data = data

class reqDict:
  """ class for requirements management 
        Dont use directly this class, but use it via inheritance
  """
  def __init__(self):
    self.reqDict = {}
  # key and body are mandatories
  def create(self, key, document, body, coverage = [], attributes = {}):
    if key in self.reqDict:
      raise error("this requirement key is still present %s"%key)
    else:
      self.add(key, document, body, coverage, attributes)
  # add a req or modify an existing one
  def add(self, key, document, body, coverage = [], attributes = {}):
    oneReq = {}
    oneReq[C_KEY_BODY] = body
    oneReq[C_KEY_DOCUMENT] = document
    if isinstance(coverage, list) != True:
      raise error("Coverage must be a list")
    self.raiseOnNotFoundRequirement(coverage)
    oneReq[C_KEY_COVERAGE] = coverage
    if isinstance(attributes, dict) != True:
      raise error("Attributes must be a dictionnary")
    oneReq[C_KEY_ATTRIBUTES] = attributes
    self.reqDict[key] = oneReq
    print("add %s"%key)
    print(oneReq)
  # get one requirement
  def __getitem__(self, key):
    return self.reqDict[key]
    print("get "+key)
  def __delitem__(self, key):
    print("del "+key)
    return self.reqDict.__delitem__(key)
  def getKeys(self):
    return self.reqDict.keys()
  def __get__(self):
    return self.reqDict
  # Check i if the provided list all tags are presents
  # an exception is done is at least one is not found
  def raiseOnNotFoundRequirement(self, listOfReq):
    if  set(listOfReq) - set(self.reqDict.keys()) != set([]):
      print(self.reqDict.keys())
      strError = "Not found requirements %s",";".join((set(listOfReq) - set(self.reqDict.keys())))
      print(strError)
      raise error(strError)
  # get a list of covered requirements
  def getListOfCoveredReq(self, listOfReq):
    cover={}
    for oneNeededReq in listOfReq:
      for item in self.reqDict.keys():
        for oneCoveredReq in self.reqDict[item][C_KEY_COVERAGE]:
          if oneCoveredReq == oneNeededReq:
            if oneNeededReq not in cover:
              cover[oneNeededReq] = []
            cover[oneNeededReq].append(item)
            print(cover)
    return cover
  # get a list of requirements from an attribute and its value
  def getListReqFromAttribute(self, attribute, value):
    listOfTags=[]
    for tag in self.reqDict.keys():
      if attribute in self.reqDict[tag][C_KEY_ATTRIBUTES]:
        if self.reqDict[tag][C_KEY_ATTRIBUTES][attribute] == value:
          listOfTags.append(tag)
    return listOfTags

# json layer
class pyReq(reqDict):
  def __init__(self, fileName):
    reqDict.__init__(self)
    print("\nopen Json %s"%fileName)
    self.fileName = fileName
    try:
      with open(self.fileName) as fp:
        self.reqDict = json.load(fp)
    except IOError:
       pass # no file
  def close(self):
    # create a sorted dictionnary for having a sorted Json file
    sortedDict=OrderedDict(sorted(self.reqDict.items(), key=lambda t: t[0]))
    #print(sortedDict)
    with open(self.fileName, mode = "w") as fp:
      json.dump(sortedDict, fp, indent=4)
    print("close Json %s"%self.fileName)
  def __del__(self):
    self.close()

    
if __name__ == '__main__':
  # 1) Test of reqDict
  print("Test of reqDict")
  requirements = reqDict()
  requirements.create("RQT_0001", "Specification1.doc", "before 10 degree a relay is set, upper than 10 degree a relay is reset")
  requirements.add("RQT_0001", "Specification1.doc", "on switch on the light is on")
  requirements.add("RQT_0002", "Specification1.doc", "on switch off the light is off")
  requirements["RQT_0002"]
  del(requirements)
  #
  # 2) Test of pyReq
  # Write a list of requirements with pyReq
  print("\n\nTest of pyReq")
  requirements = pyReq(C_PATH_WORK+"pyReq.json")
  requirements.add("RQT_0001", "Specification2.doc", "before 10 degree a relay is set, upper than 10 degree a relay is reset")
  requirements.add("RQT_0005", "Specification2.doc", "on switch on the light is on")
  del requirements["RQT_0005"]
  del(requirements)
