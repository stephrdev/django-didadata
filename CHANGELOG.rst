Changelog
=========

1.0.0 - 2020-10-15
------------------

* add django 3.0.x support
* add django 3.1.x support
* add python 3.9.x support
* drop django 1.11.x support
* drop django 2.0.x support
* drop django 2.1.x support
* drop python 3.5.x support

0.4.0 - 2020-03-30
------------------

* add django 2.2.x support
* add python 3.8.x support
* improve tests: switch from travis to github actions
* add workflow to push package to pypi easily


0.3.3 - 2019-02-14
------------------

* fix list_display of RecordAdmin


0.3.2 - 2019-02-14
------------------

* Use pytest-flake8 to improve testing
* Show metric name instead of metric id in admin view


0.3.1 - 2019-01-20
------------------

* Fix: import DjangoFilterBackend from django-filters `see django-rest-framework  <https://www.django-rest-framework.org/community/3.5-announcement/#djangofilterbackend>`_
* Refactored project to use pipenv for testing and development


0.3.0 - 2018-10-27
------------------

* Add support for Django 1.10.x
* Add support for Django 1.11.x
* Add support for Django 2.0.x
* Add support for Django 2.1.x


0.2.0 - 2016-03-12
------------------

* Replaced auto_now_add in Record.timestamp with default value to allow manual timestamps
* Extended record api with optional timestamp value


0.1.0 - 2016-02-12
------------------

* First release.
