django-didadata
===============

.. image:: https://badge.fury.io/py/django-didadata.svg
    :target: https://badge.fury.io/py/django-didadata

.. image:: https://codecov.io/gh/stephrdev/django-didadata/workflows/Testing/badge.svg?branch=master
    :target: https://codecov.io/gh/stephrdev/django-didadata/actions?query=workflow%3ATesting

.. image:: https://codecov.io/gh/stephrdev/django-didadata/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/stephrdev/django-didadata


What is django-didadata
-----------------------

`didadata` is a Django app to collect numeric data.
The app will provide graphs and notifications for collected metrics.


Prepare for development
-----------------------

A Python 3 interpreter is required. If you use pyenv with a virtualenv, follow the next steps

.. code-block:: shell

    $ cd /path/to/project-root/
    $ mkvirtualenv django-didadata
    # activate virtualenv, if not activated yet
    # and install all dev requirements:
    $ pip install -e .[dev]


Now you're ready to run the tests:

.. code-block:: shell

    $ py.test
