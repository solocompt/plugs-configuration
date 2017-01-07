=============================
Plugs Configuration
=============================

.. image:: https://badge.fury.io/py/plugs-configuration.png
    :target: https://badge.fury.io/py/plugs-configuration

.. image:: https://travis-ci.org/ricardolobo/plugs-configuration.png?branch=master
    :target: https://travis-ci.org/ricardolobo/plugs-configuration

Your project description goes here

Documentation
-------------

The full documentation is at https://plugs-configuration.readthedocs.io.

Quickstart
----------

Install Plugs Configuration::

    pip install plugs-configuration

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'plugs_configuration.apps.PlugsConfigurationConfig',
        ...
    )

Add Plugs Configuration's URL patterns:

.. code-block:: python

    from plugs_configuration import urls as plugs_configuration_urls


    urlpatterns = [
        ...
        url(r'^', include(plugs_configuration_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
