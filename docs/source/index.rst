.. NLTK Server documentation master file, created by
   sphinx-quickstart on Tue Dec 23 16:54:51 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to NLTK Server's documentation!
=======================================

NLTK Server enables you to access the features provided by NLTK Library over a REST interface. It can be easily installed on your Application VM or a seperate VM.
NLTK Server makes it easy to use NLTK with all other Languages which can make REST calls and parse JSON. 

How to Install NLTK Server
++++++++++++++++++++++++++

To install NLTK Server you will need the following:

- Python 2.7.x
- Pip

Read the guide for installing PIP here. https://pip.pypa.io/en/latest/installing.html

Steps
+++++

Clone the NLTK server repository or download Zip from Github.

.. code-block:: bash

	git clone https://github.com/preems/nltk-server

Install the requirements from Pip. 

.. code-block:: bash

	cd nltk-server
	pip install -r requirements.txt

Run NLTK Server
+++++++++++++++

.. code-block:: bash

	python wsgi.py


