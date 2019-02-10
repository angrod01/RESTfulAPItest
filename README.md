# RESTfull API test for Assurity

## API:

https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false


## Test Acceptance Criteria:

 * Name = "Carbon credits"
 * CanRelist = true
 * The Promotions element with Name = "Gallery" has a Description that contains the text "2x larger image"


## Prerequisites:

 * Python v3.0+
 * requests pip library


## Before running:

 * Install Python 3.0 or higher: https://www.python.org/downloads/
 * Install requests library running python pip install:
    `python -m pip install --upgrade pip`
    `python -m pip install requests`

## How to run the test:

Execute command: `python test_assurity.py`

Output example:
```
Running Assurity RESTful API test:
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK 
```



