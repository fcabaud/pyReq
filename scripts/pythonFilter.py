#!/usr/bin/env python
# Goal : to extract dictionnary in an xlsx file from a list of requirements
from pyReq import *
import argparse

    
if __name__ == '__main__':
  # open json file
  requirements = pyReq(C_PATH_WORK+"docExample.json")
  # get only requirements planned for sprint 2
  listOfTagsSprint2 = requirements.getListReqFromAttribute("attributeSprint", 2)
  print(listOfTagsSprint2)
  # in requirements planned for sprint 2 get the not coevered by test
  listOfTagNoCoverage = []
  for tag in listOfTagsSprint2:
    if requirements[tag][C_KEY_COVERAGE] == []:
      print("%s Not covered"%tag)  
      listOfTagNoCoverage.append(tag)
    else:
      print("%s Covered by"%tag)  
      print(requirements[tag][C_KEY_COVERAGE])
  del(requirements)