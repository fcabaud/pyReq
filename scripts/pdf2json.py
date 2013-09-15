#!/usr/bin/python
# Goal: from pdf file extract requirements and write them in json file
#    1) pdf -> temporary file ../work/output.txt via pdf2txt module 
#    2) output.txt to json file via pyReq class
#       - Input : pdfFileInput: pdf file
#       - Input : regularExpression : 
#                    regular expression for requirements extraction
#       - Output : jsonFileOutput : Json file containing requirements

import json
from pyReq import *
import pdf2txt
import sys
import re
import argparse

def serReqFromPdf(fileNameIn, regExp, fileNameOut):
  print("Extract : %s"%fileNameIn)
  pdf2txt.main(["-A", "-o", "../work/output.txt", fileNameIn])

  # 1) Read input file
  fp=open("../work/output.txt","r")
  data = fp.readlines()
  concatenatedData = "".join(data)
  # 2) provide the concatened string to regexp  
  extract = re.findall(regExp, concatenatedData)
  # 3) write json file
  requirements = pyReq(fileNameOut)
  for item in extract:
    requirements.add(item[0], fileNameIn, item[1])
  # 4) Free resources
  del(requirements)
  fp.close()

def test():
  serReqFromPdf("../in/docExample.pdf" , '(RQT_[0-9]{4})(.*)', "../work/docExample.json")
  serReqFromPdf("../in/docExample2.pdf", '(RQT_[0-9]{4})(.*)', "../work/docExample.json")
  
if __name__ == '__main__': 
  #test()
  parser = argparse.ArgumentParser(description="pdf2json ../in/docExample.pdf r'(RQT_[0-9]{4})(.*)' ../work/docExample.json")
  parser.add_argument('pdfFileInput', action="store")
  parser.add_argument('regularExpression', action="store")
  parser.add_argument('jsonFileOutput', action="store")
  result = parser.parse_args()
  arguments = dict(result._get_kwargs())  
  serReqFromPdf(arguments['pdfFileInput'], arguments['regularExpression'], arguments['jsonFileOutput'])
