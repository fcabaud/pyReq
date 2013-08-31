pyReq management of requirements in python language
===================================================

Purpose
-------

pyReq.py can be used for 
   1) Parsing requirements via regexp from pdf files
   2) Adding attributes to requirements (TargetMilestone, Maturity)
   3) Traceability from requirement to others requirements (ex: testcase)
   4) Sorting requirements
   5) Exporting requirements to testlink tool

Details
-------

Req are stored in Json file from python

pdf2json.py extract requirements from pdf to json

xlsx2json.py allows to write in Json file from xlsx (excel)
file a list of requirements + attribute and covered requirements

json2xlsx.py + a list of requirements can get back for this
list of requirements the covered req and the correspondings attributes

