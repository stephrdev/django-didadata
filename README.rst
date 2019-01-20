django-didadata
===============

.. image:: https://badge.fury.io/py/django-didadata.png
    :target: http://badge.fury.io/py/django-didadata

.. image:: https://travis-ci.org/stephrdev/django-didadata.svg?branch=master
    :target: https://travis-ci.org/stephrdev/django-didadata

.. image:: https://coveralls.io/repos/stephrdev/django-didadata/badge.svg?branch=master
  :target: https://coveralls.io/github/stephrdev/django-didadata?branch=master


What is django-didadata
-----------------------

`didadata` is a Django app to collect numeric data.
The app will provide graphs and notifications for collected metrics.


Prepare for development
-----------------------

A Python 3.6 interpreter is required in addition to pipenv.

.. code-block:: shell

    $ pipenv install --python 3.6 --dev
    $ pipenv install -e .


Now you're ready to run the tests:

.. code-block:: shell

    $ pipenv run py.test
