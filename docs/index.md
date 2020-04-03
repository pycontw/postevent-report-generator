# PyCon TW post-event report generator (rg-cli)

[![Build Status](https://cloud.drone.io/api/badges/pycontw/pycontw-postevent-report-generator/status.svg)](https://cloud.drone.io/pycontw/pycontw-postevent-report-generator)

PyCon TW post-event report generator.A cli command, rg-cli, to generate PyCon TW post-event reports. Previously known as attendee-analyzer.

rg-cli is a command line tool for you to generate a basic report of attendees, e.g. a pie chart of fields according to job titles.
Currently it only supports a csv file as raw data input.

## Prerequsite
* [Python 3.7](https://www.python.org/downloads/)
* [pipenv](https://github.com/pypa/pipenv)
    * for dependency management
    * `pip install pipenv`
* [invoke](https://github.com/pyinvoke/invoke)
    * for task management
    * `pip install invoke`

## Installation

### Fetch The Source

Fetch the source

```sh
git clone https://github.com/pycontw/pycontw-postevent-report-generator.git
```

Create a working folder to place your attendee raw data outside of the source folder so you won't commit your raw data accidentally.

```sh
mkdir pycontw-postevent-report-generator-working
```

### Create Your Own Python Virtual Environment and Install package

```sh
inv env.init-dev
```

### Install Attendees Analyzer

If you want to develop it, please run:

```sh
inv build.develop
```

If you just want to install it in your virtual environment lib, please run:

```sh
inv build.install
```

Now you should be ready to go.

### Test The Installation

```sh
inv build.test-cli
```

### Run Test Cases

```sh
inv test
```

### Example

After launching your virtual environment, issue the following command:

```sh
rg-cli --csv ./a.csv --csv ./b.csv --csv ./c.csv --yaml ./report_generator/data/generic.yaml --package-yaml ./examples/packages.yaml --sponsor-yaml ./examples/sponsors.yaml
```

Follow the prompt instruction and you will get jpg images. So far it is well tested with the data of year 2017.
