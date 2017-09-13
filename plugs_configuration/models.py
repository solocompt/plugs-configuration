from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from plugs_core import mixins

class Configuration(mixins.Timestampable, models.Model):
    """
    Configuration model
    """
    INTERNAL = 'INTERNAL'
    EXTERNAL = 'EXTERNAL'
    USER = 'USER'

    TYPES = [
        (INTERNAL, _('INTERNAL')),
        (EXTERNAL, _('EXTERNAL')),
        (USER, _('USER')),
    ]

    key = models.CharField(max_length=20)
    value = models.TextField()
    type = models.CharField(max_length=10, choices=TYPES, default=EXTERNAL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

    def validate_unique(self, exclude=None):
        if self.type != Configuration.USER and (
            (not self.pk and Configuration.objects.filter(key=self.key).exclude(type=Configuration.USER).count() > 0) or
            (self.pk and (
                    Configuration.objects.filter(key=self.key).exclude(type=Configuration.USER).count() == 1 and
                    list(Configuration.objects.filter(key=self.key).exclude(type=Configuration.USER))[0] != self
                )
            )

        ):
            raise ValidationError({'key': 'Already exists a configuration with this key.'})


    # pylint: disable=R0903
    class Meta:
        """
        Providing verbose names is recommended if
        we want to use i18n in admin site
        """
        ordering = ('pk', )
        verbose_name = _('configuration')
        verbose_name_plural = _('configurations')
