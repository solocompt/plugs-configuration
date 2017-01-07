from rest_framework import viewsets
from rest_framework import permissions

from plugs_configuration import models
from plugs_configuration import serializers

class ConfigurationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Configuration Viewset
    """
    queryset = models.Configuration.objects.all()
    serializer_class = serializers.ConfigurationSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'key'
