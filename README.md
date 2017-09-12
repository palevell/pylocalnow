# PYLOCALNOW

Returns a PyTZ object with the local time & timezone, 
with or without nanoseconds, using ISO 8601 format. (ie. 2017-09-12 12:34:56-0400)

### PREQUISITES

  - Python 3+

### INSTALLATION

  - Clone this repository
  - `cd pylocalnow`
  - `[sudo] pip3 install .`
  
### USAGE

  - BASH prompt: `bin/localnow`
  - In a Python module: `from localnow import *`
  - Python prompt: `from localnow import localnow; print(localnow())`

##### BASH Examples (Eastern Daylight Time)
```
$ localnow --help

usage: localnow [-h] [-n] [-i]

Returns a PyTZ object with the local time & timezone

optional arguments:
  -h, --help  show this help message and exit
  -n, --nano  include nanoseconds
  -i, --iso   use ISO 8601 format

$ localnow --iso --nano
2017-09-12T12:34:56.789012-0400

$ localnow
2017-09-12 12:34:56-0400
```

##### Python Examples
```
>>> from localnow import localnow
>>> print(localnow())
2017-09-12 12:34:56.084246-04:00

>>> localnow().isoformat
2017-09-12T12:34:56.084342-04:00

>>> localnow().replace(microsecond=0)
2017-09-12 12:34:56-04:00

>>> localnow().replace(microsecond=0).isoformat()
2017-09-12T12:34:56-04:00
```

### BACKGROUND

Generally speaking, support for timezone-aware applications is
inadequate.  This became painfuly obvious during my work on the
**_iWarehouse_**&trade; project, while collecting data from vehicles 
in over 60 countries.

This module will form the base for future time-related projects.


