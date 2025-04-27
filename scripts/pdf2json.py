#!/usr/bin/python
# Goal: from pdf file extract requirements and write them in json file
#    1) pdf -> temporary file ../work/output.txt via pdftotext module 
#    2) output.txt to json file via pyReq class
#       - Input : pdfFileInput: pdf file
#       - Input : regularExpression : 
#                    regular expression for requirements extraction
#       - Output : jsonFileOutput : Json file containing requirements

from pyReq import pyReq, C_PATH_IN, C_PATH_WORK
from pypdf import PdfReader
import re
import argparse

def get_req_from_pdf(fileNameIn, regExp, fileNameOut):
  """ transform pdf file fileNameIn in requirements 
       in json file fileNameOut via reg exp regExp
  
     :arg fileNameIn: pdf file containing requirements
     :type fileNameIn: string

     :arg regExp: regular expression
     :type regExp: string

     :arg fileNameOut: Json file
     :type fileNameOut: string
  """
  print("Extract : %s"%fileNameIn)

  fp=open("../work/output.txt","w")
  reader = PdfReader(fileNameIn)
  #reader.isEncrypted  # is True
  for item in range(len(reader.pages)):
    text=reader.pages[item].extract_text()
    #print(text)
    #print("next page")
    fp.writelines(text)
  fp.close()

  # 1) Read input file
  fp=open("../work/output.txt","r")
  data = fp.readlines()
  concatenatedData = "".join(data)
  #
  # 2) provide the concatened string to regexp  
  extract = re.findall(regExp, concatenatedData)
  #
  # 3) write json file
  requirements = pyReq(fileNameOut)
  for item in extract:
    requirements.add(item[0], fileNameIn, item[1])
  #
  # 4) Free resources
  del(requirements)
  fp.close()

def test():
  get_req_from_pdf("../in/docExample.pdf" , '(RQT_[0-9]{4})(.*)', "../work/docExample.json")
  get_req_from_pdf("../in/docExample2.pdf", '(RQT_[0-9]{4})(.*)', "../work/docExample.json")
  
if __name__ == '__main__': 
  #test()
  #parser = argparse.ArgumentParser(description="pdf2json %sdocExample.pdf r'(RQT_[0-9]{4})(.*)' %sdocExample.json"%(C_PATH_IN, C_PATH_WORK))
  parser = argparse.ArgumentParser(description="pdf2json %sdocExample.pdf '(RQT_[0-9]{4})(.*)' %sdocExample.json"%(C_PATH_IN, C_PATH_WORK))
  parser.add_argument('pdfFileInput', action="store")
  parser.add_argument('regularExpression', action="store")
  parser.add_argument('jsonFileOutput', action="store")
  result = parser.parse_args()
  arguments = dict(result._get_kwargs())  
  get_req_from_pdf(arguments['pdfFileInput'], arguments['regularExpression'], arguments['jsonFileOutput'])
