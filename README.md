# Attendees-analyzer (atta)

Attendees-analyzer (atta) is a command line tool for you to generate a basic report of attendees, e.g. a pie chart of fields according to job titles.  
Currently it only supports a csv file as raw data input.

## Prerequsite
* [Python 3.7](https://www.python.org/downloads/)
* [pipenv](https://github.com/pypa/pipenv)
    * for dependency management
* [invoke](https://github.com/pyinvoke/invoke)
    * for task management

## Installation

### Fetch The Source

Fetch the source

```sh
git clone https://github.com/tai271828/attendees-analyzer.git
```

Create a working folder to place your attendee raw data outside of the source folder so you won't commit your raw data accidentally.

```sh
mkdir attendees-analyzer-working
```

### Create Your Own Python Virtual Environment and Install package

```sh
inv init-dev
```

### Install Attendees Analyzer

If you want to develop it, please run:

```sh
inv develop
```

If you just want to install it in your virtual environment lib, please run:

```sh
inv install
```

Now you should be ready to go.

### Test The Installation

```sh
pipenv run atta
```

## Run Test Cases

```sh
inv test
```

## Example

After launching your virtual environment, issue the following command:

```sh
atta --csv ./a.csv --csv ./b.csv --csv ./c.csv
--yaml ./atta/data/generic.yaml
--package-yaml ./examples/packages.yaml
--sponsor-yaml ./examples/sponsors.yaml
```

Follow the prompt instruction and you will get jpg images. So far it is well tested with the data of year 2017.
