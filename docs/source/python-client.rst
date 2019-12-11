=============
Python Client
=============

************
Installation
************


You may create the necessary python environment with Anaconda::

    cd /path/to/willitsync
    conda env create -f=environment.yml -n willitsync
    conda activate willitsync
    # TODO: finalize SlenderNodes/schema_org install

You may start the server as follows::

    cd python-flask
    python -m openapi_server

To install the client tools with Anaconda, please execute the following
from the ``python-client`` directory::

    cd /path/to/willitsync/python-client
    python setup.py install

The client tools can be installed and run on another machine, but if that is the case, the
``willitsync`` environment should be recreated there, and an SSH tunnel
should be made from the client machine to the server machine, i.e.::

    $ ssh -L 8080:server:8080


*****
Usage
*****

::

    $ willitsync --help
    Usage: willitsync [OPTIONS] COMMAND [ARGS]...
    
    Options:
      -v, --verbosity LVL  Either CRITICAL, ERROR, WARNING, INFO or DEBUG
      --help               Show this message and exit.
    
    Commands:
      get-scivalid
      get-so
      get-sovalid
      robot
      scivalid
      sitemap
      sovalid

