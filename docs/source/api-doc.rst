=================
API Documentation
=================

Sentence Tokenizer
==================

.. http:post:: /sent_tokenize

Takes a document and return a array of sentences. Uses nltk.sent_tokentize.

**Example request**:

.. sourcecode:: http

  POST /sent_tokenize HTTP/1.1
  Host: example.com
  Accept: application/json

  Lorem Ipsum is simply dummy text of the printing. Lorem Ipsum has been the industry's standard dummy text, when an unknown printer took a galley of type. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

**Example response**:

.. sourcecode:: http

  HTTP/1.1 200 OK
  Vary: Accept
  Content-Type: application/json

  {
    "result": [
      "Lorem Ipsum is simply dummy text of the printing.", 
      "Lorem Ipsum has been the industry's standard dummy text, when an unknown printer took a galley of type.", 
      "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
    ], 
    "status": "success"
  }

Word Tokenizer
==============

.. http:post:: /word_tokenize

Takes a sentence and tokenizes into words. Uses nltk.word_tokenize.

**Example request**:

.. sourcecode:: http

  POST /word_tokenize HTTP/1.1
  Host: example.com
  Accept: application/json

  Lorem Ipsum is simply dummy text of the printing.

**Example response**:

.. sourcecode:: http

  HTTP/1.1 200 OK
  Content-Length: 164
  Content-Type: application/json
  Date: Wed, 24 Dec 2014 01:58:15 GMT
  Server: Werkzeug/0.9.6 Python/2.7.6

  {
    "result": [
      "Lorem", 
      "Ipsum", 
      "is", 
      "simply", 
      "dummy", 
      "text", 
      "of", 
      "the", 
      "printing"
    ], 
    "status": "success"
  }

Part of Speech Tagging
======================

.. http:post:: /pos_tag

Takes a array of words tokenized by the word tokenizer.

**Example request**:

.. sourcecode:: http

  POST /pos_tag HTTP/1.1
  Host: example.com
  Accept: application/json

  [
    "Lorem", 
    "Ipsum", 
    "is", 
    "simply", 
    "dummy", 
    "text", 
    "of", 
    "the", 
    "printing"
  ]

**Example response**:

.. sourcecode:: http

  HTTP/1.1 200 OK
  Content-Length: 164
  Content-Type: application/json
  Date: Wed, 24 Dec 2014 02:12:15 GMT
  Server: Werkzeug/0.9.6 Python/2.7.6
  
  {
  "result": [
    [
      "Lorem", 
      "NNP"
    ], 
    [
      "Ipsum", 
      "NNP"
    ], 
    [
      "is", 
      "VBZ"
    ], 
    [
      "simply", 
      "RB"
    ], 
    [
      "dummy", 
      "JJ"
    ], 
    [
      "text", 
      "NN"
    ], 
    [
      "of", 
      "IN"
    ], 
    [
      "the", 
      "DT"
    ], 
    [
      "printing", 
      "NN"
    ]
  ], 
  "status": "success"
  }

Stemming
========

.. http:post:: /stem/(string:algorithm)

Takes an array of words and return the stem of words. The valid algorithms are 'porter', 'lancaster' and 'snowball'.

**Example request**:

.. sourcecode:: http

  POST /stem/porter HTTP/1.1
  Host: example.com
  Accept: application/json

  [
    "the", 
    "buses", 
    "are", 
    "crowded"
  ]

**Example response**:

.. sourcecode:: http

  HTTP/1.1 200 OK
  Content-Length: 212
  Content-Type: application/json
  Date: Wed, 24 Dec 2014 06:45:29 GMT
  Server: Werkzeug/0.9.6 Python/2.7.6

  {
  "result": [
    [
      "the", 
      "the"
    ], 
    [
      "buses", 
      "buse"
    ], 
    [
      "are", 
      "are"
    ], 
    [
      "crowded", 
      "crowd"
    ]
  ], 
  "status": "success"
  }  
