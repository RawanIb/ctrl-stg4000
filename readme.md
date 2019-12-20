[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://en.wikipedia.org/wiki/MIT_License) [![pytest-status](https://github.com/pyreiz/ctrl-stg4000/workflows/pytest/badge.svg)](https://github.com/pyreiz/ctrl-stg4000/actions) [![Coverage Status](https://coveralls.io/repos/github/pyreiz/ctrl-stg4000/badge.svg?branch=develop)](https://coveralls.io/github/pyreiz/ctrl-stg4000?branch=develop) [![Documentation Status](https://readthedocs.org/projects/ctrl-stg4000/badge/?version=latest)](https://ctrl-stg4000.readthedocs.io/en/latest/?badge=latest)

Welcome to STG4000's documentation!
===================================

This documentation explains the python package wrapping the [C# .dll](https://www.multichannelsystems.com/software/mcsusbnetdll) offered by
multichannelsystems to control their STG4000 range of electrical stimulators.

Installation
------------

``` bash

    git clone https://github.com/pyreiz/app-stg4000
    cd app-stg4000
    pip install -r requirements.txt
    pip install -e .
    #download and install the dll from mulitchannelsystems
    python -m stg.install
```
Because of this, the pacakage only works on Windows. If the package is run on Linux, skip the installation of the requirements. On linux, the package automatically mocks the interface to the STG4000. This allows to run tests and build documentation, and can help when you write scripts for your experiments.

Testing
-------

Connect your oscilloscope and start the following example:

``` python

   from stg.api import PulseFile, STG4000
   stg = STG4000()
   stg.download(0, *PulseFile().compile())
   stg.start_stimulation([0])
```
You can run full tests using pytest, mypy or everything with :code: `make test` from the root of the package. By default, downloading the dll is not tested, but can be turned on with :code:`pytest -m "install"`.
