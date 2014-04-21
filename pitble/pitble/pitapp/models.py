from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Pitble(models.Model):
    text = models.TextField(verbose_name=_('Text'))
    owner = models.ForeignKey(User, verbose_name=_('Owner'))

    def __str__(self):
        return self.text