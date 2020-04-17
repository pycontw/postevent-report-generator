# PyCon TW post-event report generator (rg-cli)

[![Python Check](https://github.com/pycontw/pycontw-postevent-report-generator/workflows/python%20check/badge.svg)](https://github.com/commitizen-tools/pycontw-postevent-report-generator/actions) [![PyPI Package latest release](https://img.shields.io/pypi/v/pycontw-report-generator.svg?style=flat-square)](https://pypi.org/project/pycontw-report-generator/)

PyCon TW post-event report generator.A cli command, rg-cli, to generate PyCon TW post-event reports. Previously known as attendee-analyzer.

rg-cli is a command line tool for you to generate a basic report of attendees, e.g. a pie chart of fields according to job titles.
Currently it only supports a csv file as raw data input.

## Prerequsite
* [Python 3.7](https://www.python.org/downloads/)

## Installation

```sh
python -m pip install pycontw-report-generator
```

### Usage

```sh
$ python -m rg-cli --help

Usage: rg-cli [OPTIONS]

Options:
  --csv TEXT                      Read csv format data  [required]
  --talks-csv TEXT                CSV file for talks  [required]
  --proposed-talks-csv TEXT       CSV file for proposed talks  [required]
  --booth-csv TEXT                CSV file for booth checking  [required]
  --interactive / --no-interactive
                                  Quiet mode. Useful for automation. True for
                                  no prompt.  [default: False]
  --cjk-support / --no-cjk-support
                                  Enable CJK support in the plot or not.
                                  [default: False]
  --conf TEXT                     Configuration file of how to analyze
  --yaml TEXT                     Report yaml file to describe how a report
                                  would be  [required]
  --package-yaml TEXT             Package yaml file to describe how a package
                                  is defined  [required]
  --sponsor-yaml TEXT             Sponsor yaml file to describe how a sponsor
                                  is defined  [required]
  --output-path TEXT              Where the reports exported  [default: /tmp]
  --help                          Show this message and exit.
```

Create a working folder to place your attendee raw data outside of the source folder so you won't commit your raw data accidentally.

```sh
mkdir ../pycontw-postevent-report-generator-working
```

### Example

After launching your virtual environment, issue the following command:

```sh
rg-cli --csv ./a.csv --csv ./b.csv --csv ./c.csv --yaml ./report_generator/data/generic.yaml --package-yaml ./examples/packages.yaml --sponsor-yaml ./examples/sponsors.yaml
```

Follow the prompt instruction and you will get jpg images. So far it is well tested with the data of year 2017.

## How to contribute
Please see the [Contribute](contribute.md) for further details.
