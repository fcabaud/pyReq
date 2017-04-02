pyReq management of requirements in python language
===================================================


Purpose
-------

EXTRACTION of REQUIREMENTS from WORD DOCUMENTS
See examples after Installation and run demo chapter

Installation and run demo 
-------------------------

1. Linux Ubuntu

    - git clone https://github.com/jaepil/pdfminer3k.git

    - git clone https://github.com/fcabaud/pyReq.git

    - sudo pip3 install openpyxl

    - cd pyReq 

2. Windows : NOT TESTED !!

  - install pdfminer

     - 2.x version is here

    https://pypi.python.org/pypi/pdfminer/

     - 3.x version is here

    https://pypi.python.org/pypi/pdfminer3k

    **c:\\python27\\python.exe setup.py install**

  - install openpyxl

    https://pypi.python.org/pypi/openpyxl  

    **c:\\Python27\\python.exe  setup.py install**

  - install setuptools

   https://pypi.python.org/pypi/setuptools/

   **c:\\Python27\\python.exe  setup.py install**

  - enjoy !

    **cd scripts**

    **test.bat**

Examples
-------

pyReq.py can be used for :
   1. **Parsing requirements via regexp from pdf files**

    python3 ./pdf2json.py ../in/docExample.pdf "(RQT_[0-9]{4})(.*)" ../work/docExample.json


    will extract requirements of docExample.pdf via a regular expression in docExample.json

   2. **Adding attributes to requirements (TargetMilestone, Maturity)**

     python3 ./xlsx2json.py ../in/reqListSprints.xlsx ../work/docExample.json

     will add attributes of requirements from reqListSprints.xlsx to docExample.json

   3. **Traceability from requirement to others requirements (ex: testcase)**

     python3 ./xlsx2json.py ../in/reqListCoverage.xlsx ../work/docExample.json

     will provides traceability between requirements from reqListCoverage.xlsx to docExample.json

   4. **Sorting requirements**

     python3 ./json2xlsx.py ../work/docExample.json ../out/reqListStatusKO.xlsx

     will extract requirements which have tests failed from docExample.json to reqListStatusKO.xlsx

   5. **Exporting requirements to testlink tool**

     python3 ./json2xlsx.py ../work/docExample.json ../out/testlinkInput.csv

     will export a testlink csv file from docExample.json
  
Directories goal 
----------------

- doc: minimalist schema trying to explain how it works
- in : input files (pdf), xlsx (input): your input(s)
- out : result of an extraction : dont modify it
- work: permanent requirements storage (like a database) in json format
- scripts: python scripts (see doc in doc file)

Doc
-------

Req are stored in Json file from python

- pdf2json.py extract requirements from pdf to json

- xlsx2json.py allows to write in Json file from xlsx (excel)
  file a list of requirements + attribute and covered requirements

- json2xlsx.py + a list of requirements can get back for this
  list of requirements the covered req and the correspondings attributes

![graphic](doc/pyReq.svg)

