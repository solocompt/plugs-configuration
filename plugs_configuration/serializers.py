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
        fields = ('key', 'value', 'type', 'user', 'created', 'updated')
        read_only_fields = ('type', 'user')
