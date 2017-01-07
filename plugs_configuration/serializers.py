from rest_framework import serializers

from plugs_configuration.models import Configuration

class ConfigurationSerializer(serializers.ModelSerializer):
    """
    Configuration Serializer
    """
    class Meta:
        """
        Metaclass definition
        """
        model = Configuration
        fields = ('key', 'value', 'created', 'updated')
