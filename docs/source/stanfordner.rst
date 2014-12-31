========================
Named Entity Recognition
========================

.. http:post:: /stanfordNER

This API uses the Stanford NER Library. You can read more details about this project on http://nlp.stanford.edu/software/CRF-NER.shtml. 

The API requires JRE to be installed.

**Example request**:

.. sourcecode:: http

  POST /stanfordNER HTTP/1.1
  Host: example.com
  Accept: application/json

  Rami Eid is studying at Stony Brook University in NY.

**Example response**:

.. sourcecode:: http

  HTTP/1.1 200 OK
  Content-Length: 479
  Content-Type: application/json
  Date: Tue, 30 Dec 2014 19:23:14 GMT
  Server: Werkzeug/0.9.6 Python/2.7.6

  {
  "result": [
    [
      "Rami", 
      "PERSON"
    ], 
    [
      "Eid", 
      "PERSON"
    ], 
    [
      "is", 
      "O"
    ], 
    [
      "studying", 
      "O"
    ], 
    [
      "at", 
      "O"
    ], 
    [
      "Stony", 
      "ORGANIZATION"
    ], 
    [
      "Brook", 
      "ORGANIZATION"
    ], 
    [
      "University", 
      "ORGANIZATION"
    ], 
    [
      "in", 
      "O"
    ], 
    [
      "NY", 
      "O"
    ]
  ], 
  "status": "success"
  }