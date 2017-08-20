from django.db.models import Q

from rest_framework import viewsets

from plugs_core.permissions import IsOwnerOrReadOnly

from plugs_configuration.models import Configuration
from plugs_configuration import serializers

class ConfigurationViewSet(viewsets.ModelViewSet):
    """
    Configuration Viewset
    """
    queryset = Configuration.objects.exclude(type=Configuration.INTERNAL)
    serializer_class = serializers.ConfigurationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'key'

    def perform_create(self, serializer):
        """
        Only user configurations can be created using the api
        """
        serializer.save(user=self.request.user, type=Configuration.USER)

    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return self.queryset.exclude(type=Configuration.USER)
        else:
            return self.queryset.filter(Q(user=self.request.user) | Q(type=Configuration.EXTERNAL))
