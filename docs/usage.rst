=====
Usage
=====

To use Plugs Configuration in a project, add it to your `INSTALLED_APPS`:

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
