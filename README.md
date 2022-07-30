# Address book

This is addressbook Concept created using Fastapi Framework.


## Features

* Create addressbook with given the fields first_name, Last_name, latitude and longitude.
* Udate addressbook with particuler id
* Delete addressbook with particuler id
* Retrieve the address of the particuler id it converts the latitude and loggitude to the Full address


## Prerequisites

Be sure you have the following installed on your development machine:

+ Python >= 3.7
+ uvicorn Server
+ Fastapi
+ geopy
+ Django
+ Git
+ pip
+ Virtualenv (virtualenvwrapper is recommended)

## Requirements

+ python
+ fastapi
+ uvicorn
+ sqlalchemy
+ sqlalchemy-utils
+ geopy
+ django

## Install Requirements

Run the below statements
```bash
> pip install -r requirements.txt
```

## Project Installation

To setup a local development environment:

Create a virtual environment in which to install Python pip packages. With [virtualenv](https://pypi.python.org/pypi/virtualenv),
```bash
    python -m venv addressapi-env        # create a virtualenv
    address-api\Scripts\activate.bat   # activate the Python virtualenv 
```

Install development dependencies,
```bash
pip install -r requirements.txt
```

Run the web application locally,
```bash
uvicorn address.addressapi:app --reload # 127.0.0.1:8000
```

