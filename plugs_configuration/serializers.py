from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from plugs_configuration.models import Configuration

class ConfigurationSerializer(serializers.ModelSerializer):
    """
    Configuration Serializer
    """
    def create(self, validated_data):
        if Configuration.objects.filter(type=Configuration.USER, key=validated_data['key'], user=validated_data['user']).count() > 0:
            raise serializers.ValidationError({'key': 'You already have a configuration with this key.'})
        return super(ConfigurationSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if (Configuration.objects.filter(type=Configuration.USER, key=validated_data['key'], user=instance.user).count() == 1 and
            list(Configuration.objects.filter(type=Configuration.USER, key=validated_data['key'], user=instance.user))[0] != instance):
            raise serializers.ValidationError({'key': 'You already have a configuration with this key.'})
        return super(ConfigurationSerializer, self).update(instance, validated_data)

    class Meta:
        """
        Metaclass definition
        """
        model = Configuration
        fields = ('key', 'value', 'type', 'user', 'created', 'updated')
        read_only_fields = ('type', 'user')

