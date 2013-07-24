#!/usr/RQT/env python
# Tests of Requirement management stored in a Json file
import pyReq
import pdf2json
import xlsx2json
import json2xlsx

if __name__ == '__main__':
  pdf2json.test()
  xlsx2json.test()
  json2xlsx.test()