.. contents::

======
Pitble
======

Information
===========

.. image:: https://travis-ci.org/openwebinars-django/pitble.svg
    :target: https://travis-ci.org/openwebinars-django/pitble


.. image:: https://coveralls.io/repos/openwebinars-django/pitble/badge.png
  :target: https://coveralls.io/r/openwebinars-django/pitble


.. image:: https://badge.fury.io/py/pitble.png
    :target: https://badge.fury.io/py/pitble

.. image:: https://pypip.in/d/pitble/badge.png
    :target: https://pypi.python.org/pypi/pitble


Pitble is a python microblog


Installation
============

* In your settings:

::

    INSTALLED_APPS = (
        ...
        'pitble',
        'bootstrap3',
    )


    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'pitble.context_processors.i18n',

    )


    MIDDLEWARE_CLASSES = (
        ...
        'django.middleware.locale.LocaleMiddleware',
        'pitble.middleware.LocaleMiddleware',
    )

    AUTH_USER_MODEL = 'pitble.User'

    LOGIN_URL = '/sign-in/'
    
* In your urls:

::
    
    urlpatterns = patterns('',
        ...
        url(r'^', include('pitble.urls')),
    )
