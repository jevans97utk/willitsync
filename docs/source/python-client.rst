=============
Python Client
=============

************
Installation
************


You may install the server software requirements using Anaconda::

    conda env create -f=environment.yml -n willitsync
    # TODO: finalize SlenderNodes/schema_org install

You may start the server as follows::

    python3 -m openapi_server

To install the client tools with Anaconda, please execute the following
from the ``python-client`` directory::

    conda env create -f=environment.yml
    conda activate willitsync
    python setup.py install
    # TODO: finalize SlenderNodes/schema_org install

The client tools can be installed and run on another machine, but if that is the case, an 
SSH tunnel should be made from the client machine to the server machine, i.e.::

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

