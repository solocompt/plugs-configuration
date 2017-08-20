from django.contrib import admin

from plugs_configuration.models import Configuration

class ConfigurationAdmin(admin.ModelAdmin):
    """
    Configuration Model Admin
    """
    list_display = ('key', 'value', 'type', 'user')

admin.site.register(Configuration, ConfigurationAdmin)
