#!/usr/bin/env python
import json
from pyReq import *
import pdf2txt
import sys
import re
import argparse

def serReqFromPdf(fileNameIn, regExp, fileNameOut):
  #pdf2txt.main(sys.argv)
  #pdf2txt.main(["-A", fileNameIn])
  print("Extract : %s"%fileNameIn)
  pdf2txt.main(["-A", "-o", "../work/output.txt", fileNameIn])

  fp=open("../work/output.txt","r")
  data = fp.readlines()
  #print(data)
  requirements = pyReq(fileNameOut)
  for item in data:
    extract = re.findall(regExp, item)
    if extract != []:
      #print(extract[0])
      requirements.add(extract[0][0], fileNameIn, extract[0][1])
  # write json file
  del(requirements)
  fp.close()

def test():
  serReqFromPdf("../in/docExample.pdf" , r'(RQT_[0-9]{4})(.*)', "../work/docExample.json")
  serReqFromPdf("../in/docExample2.pdf", r'(RQT_[0-9]{4})(.*)', "../work/docExample.json")
  
if __name__ == '__main__': 
  #test()
  parser = argparse.ArgumentParser(description="pdf2json ../in/docExample.pdf r'(RQT_[0-9]{4})(.*)' ../work/docExample.json")
  parser.add_argument('pdfFileInput', action="store")
  parser.add_argument('regularExpression', action="store")
  parser.add_argument('jsonFileOutput', action="store")
  result = parser.parse_args()
  arguments = dict(result._get_kwargs())  
  serReqFromPdf(arguments['pdfFileInput'], arguments['regularExpression'], arguments['jsonFileOutput'])
