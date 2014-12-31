============
Installation
============

Prerequisites
+++++++++++++
To install NLTK Server you will need the following:

- Python 2.7.x
- Pip

Read more on installing PIP here. https://pip.pypa.io/en/latest/installing.html

How to Install
++++++++++++++

1. Clone the NLTK server repository.

.. code-block:: bash

  git clone https://github.com/preems/nltk-server

Or download latest Zip from Github:

2. Install dependencies from pip.

.. code-block:: bash

  cd nltk-server
  pip install -r requirements.txt

Some linux distros might require to use sudo.

3. Install JRE ( only required for Stanford NER ).

Installation of JRE is specific to Operating system your running on. For Ubuntu, it can be installed by running following commands

.. code-block:: bash
  
  $ sudo apt-get update    
  $ sudo apt-get default-jre


Run NLTK Server
+++++++++++++++

.. code-block:: bash

    python wsgi.py