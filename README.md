
Attendees-analyzer (atta) is a command line tool for you to generate a basic
 report of attendees, e.g. a pie chart of fields according to job titles. 
 Currently it only supports a csv file as raw data input.

# Installation

## Fetch The Source

Fetch the source

```git clone https://github.com/tai271828/attendees-analyzer.git```

Create a working folder to place your attendee raw data outside of the 
source folder so you won't commit your raw data accidentally.

```mkdir attendees-analyzer-working```

## Create Your Own Python Virtual Environment

Create the working virtual environment

```virtualenv -p python3 ./attendees-analyzer-working/venv```

Activate your virtual environment by

```source ./attendees-analyzer-working/venv/bin/activate```

## Install The Prerequisite Modules

Go the source folder

```pip install -r requirements.txt```


## Install Attendees Analyzer

If you want to develop it, please run:

```python setup.py develop```

If you just want to install it in your virtual environment lib, please run:

```python setup.py install```

Now you should be ready to go.

## Test The Installation

Go to the test folder and execute the unit tests.

```
cd test
./title.py
```
If you get something like this, it means everything should work as expected.

```
.
----------------------------------------------------------------------
Ran 1 test in 0.014s

OK
```


# Example

After launching your virtual environment, issue the following command:

```atta --readcsv ../attendees-analyzer-working/2017Attendees.csv```

Follow the prompt instruction and you will get jpg images. So far it is well
 tested with the data of year 2017.
 
