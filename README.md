pyReq management of requirements in python language
===================================================

Purpose
-------

pyReq.py can be used for 
   1. Parsing requirements via regexp from pdf files
   2. Adding attributes to requirements (TargetMilestone, Maturity)
   3. Traceability from requirement to others requirements (ex: testcase)
   4. Sorting requirements
   5. Exporting requirements to testlink tool

Installation and run demo 
-------------------------

1. Linux Ubuntu

  - install pdfminer (for pdf management):

    **sudo apt-get install python-pdfminer**

  - install openpyxl (for xlsx management):

    **sudo apt-get install python-openpyxl**

  - enjoy !

    **cd scripts**

    **python tests.py**

2. Windows

  - install openpyxl

    https://pypi.python.org/pypi/openpyxl  

    **c:\Python27\python.exe  setup.py install**

  - enjoy !

    **cd scripts**

    **python tests.py**

    **cd scripts**

    **test.bat**
  
Directories goal 
----------------

- doc: minimalist schema trying to explain how it works
- in : input files (pdf), xlsx (input): your input(s)
- out : result of an extraction : dont modify it
- work: permanent requirements storage (like a database) in json format
- scripts: python scripts (see doc in doc file)

Details
-------

Req are stored in Json file from python

- pdf2json.py extract requirements from pdf to json

- xlsx2json.py allows to write in Json file from xlsx (excel)
  file a list of requirements + attribute and covered requirements

- json2xlsx.py + a list of requirements can get back for this
  list of requirements the covered req and the correspondings attributes
