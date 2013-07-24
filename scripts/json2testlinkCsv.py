#!/usr/bin/env python
# Goal : to extract dictionnary in an xlsx file from a list of requirements
from pyReq import *
import argparse

class getXlsx(pyReq):
  def getXlsx(self, listOfReq = [], testlinkFileName = 'getReq.csv'):
    #dictReq = self.get(listOfReq)
    #print(listOfReq)
    if listOfReq == []:
      listOfReq = self.reqDict.keys()
    print(listOfReq)
    fp = open(testlinkFileName, 'w')
    for tag in listOfReq:
      # "RQT_SPR_FonctionX_0001","RQT_SPR_FonctionX_0001","La fonctionX doit etre mise en place au dessus de 30 degres.",1,"F",1,1
      print(tag)
      print(self.reqDict[tag][C_KEY_BODY])
      fp.write('"%s","%s","%s",1,"F",1,1\n'%(tag,tag,self.reqDict[tag][C_KEY_BODY]))
    fp.close()
    print("Write csv file %s"%testlinkFileName)

def test():
  getReqInstance = getXlsx(C_PATH_WORK+"docExample.json")
  #listOfTags = ['RQT_0001','RQT_0003']
  #print(getReqInstance.getKeys())
  # Example 1 : get all requirements not covered of sprint 2 : what validation team has to do
  listOfTagsSprint2 = getReqInstance.getListReqFromAttribute("attributeSprint", 2)
  for tag in listOfTagsSprint2:
    if getReqInstance[tag][C_KEY_COVERAGE] == []:
      print("%s Not covered"%tag)  
  getReqInstance.getXlsx(listOfTagsSprint2, C_PATH_OUT+'reqListSprint2NotCovered.xlsx')  
  # Example 2 : get all requirements covered by a KO test : what development team has to do
  listOfTagsSprint1 = getReqInstance.getListReqFromAttribute("attributeStatus", "KO")
  getReqInstance.getXlsx(listOfTagsSprint1, C_PATH_OUT+'reqListStatusKO.xlsx')  
    
if __name__ == '__main__':
  #test()
  parser = argparse.ArgumentParser(description='json2xlsx ..\work\docExample.json ..\out\testlinkInput.csv')
  parser.add_argument('jsonFileInput', action="store")
  parser.add_argument('testlinkcsvFileOutput', action="store")
  result = parser.parse_args()
  arguments = dict(result._get_kwargs())  
  #print(arguments['xlsxFileInput'])
  #print(arguments['jsonFileOutput'])
  getReqInstance = getXlsx(arguments['jsonFileInput'])
  #listOfTagsSprint1 = getReqInstance.getListReqFromAttribute("attributeStatus", "KO")
  getReqInstance.getXlsx([], arguments['testlinkcsvFileOutput'])  
