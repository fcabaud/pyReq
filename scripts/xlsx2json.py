#!/usr/bin/env python
# Goal : to extract dictionnary in an xlsx file from a list of requirements
import os
from pyReq import *
from openpyxl import load_workbook
import argparse

class setXlsx(pyReq):
  # 3 fields are mandatories : tag, body and document name
  def checkMandatoriesFieldNames(self, line1Names):
    if C_KEY_TAG not in line1Names: 
      raise error(" %s not found in first line of xls file"%C_KEY_TAG)
    if C_KEY_BODY not in line1Names: 
      raise error(" %s not found in first line of xls file"%C_KEY_BODY)
    if C_KEY_DOCUMENT not in line1Names: 
      raise error(" %s not found in first line of xls file"%C_KEY_DOCUMENT)
  def setXlsx(self, excelName = 'setReq.xlsx'):
    print(excelName)
    wb = load_workbook(excelName)
    ws = wb.get_active_sheet()
    # 1) Get the column number from the name and check mandatories name
    line1Names = {}
    for item in range(ws.get_highest_column()):
      if ws.cell(row = 0, column = item).value != None:
        #print(ws.cell(row = 0, column = item).value)
        line1Names[ws.cell(row = 0, column = item).value] = item
    #print(line1Names)
    # Check mandatories fields
    self.checkMandatoriesFieldNames(line1Names)    
    # Get attributes names
    attributesListName=[]
    #print(ws.get_highest_column())
    for item in line1Names.keys():
      #print(item)
      if C_KEY_ATTRIBUTES in item:
        attributesListName.append(item)
    #print(attributesListName)
    # 2) Import data
    for line in range(ws.get_highest_row()):
      if line > 0:
        # 2.1) Get tag field
        tag      = ws.cell(row = line, column = line1Names[C_KEY_TAG]).value
        # 2.2) Get body
        body     = ws.cell(row = line, column = line1Names[C_KEY_BODY]).value
        # 2.2) Get document name
        document = ws.cell(row = line, column = line1Names[C_KEY_DOCUMENT]).value
        # 3) Optionnal fields
        coverage   = []
        if C_KEY_COVERAGE in line1Names:
          if ws.cell(row = line, column = line1Names[C_KEY_COVERAGE]).value != None:
            coverage   = ws.cell(row = line, column = line1Names[C_KEY_COVERAGE]).value.split(";")
        #print("coverage")
        #print(self.reqDict[tag][C_KEY_COVERAGE])
        #self.reqDict[tag][C_KEY_ATTRIBUTES] = ws.cell(row = line, column = line1Names[C_KEY_ATTRIBUTES]).value
        attributesDict = {}
        for attribute in attributesListName:
          if ws.cell(row = line, column = line1Names[attribute]).value != None:
            #self.reqDict[tag][C_KEY_ATTRIBUTES][attribute]   = ws.cell(row = line, column = line1Names[attribute]).value
            attributesDict[attribute]   = ws.cell(row = line, column = line1Names[attribute]).value

        # write in internal structure
        self.add(tag, document, body, coverage, attributesDict)

def test():        
  getReqInstance = setXlsx(C_PATH_WORK+"docExample.json")
  getReqInstance.setXlsx(C_PATH_IN+'reqListCoverage.xlsx')  
  getReqInstance.setXlsx(C_PATH_IN+'reqListSprints.xlsx')  
  getReqInstance.setXlsx(C_PATH_IN+'reqListSprints_OnlyStatus.xlsx')  
        
if __name__ == '__main__':
  #test()
  parser = argparse.ArgumentParser(description='xlsx2json ..\in\reqListCoverage.xlsx ..\work\docExample.json')
  parser.add_argument('xlsxFileInput', action="store")
  parser.add_argument('jsonFileOutput', action="store")
  result = parser.parse_args()
  arguments = dict(result._get_kwargs())  
  #print(arguments['xlsxFileInput'])
  #print(arguments['jsonFileOutput'])
  getReqInstance = setXlsx(arguments['jsonFileOutput'])
  getReqInstance.setXlsx(arguments['xlsxFileInput'])  
  