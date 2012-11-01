# coding=utf-8
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
# Create your models here.

CHAR_FIELD_MAX_LEN = 200



class Dictionary(models.Model):
    """
        Dictionary item. Dictionary
    """
    class Meta:
        verbose_name = _(u"Dictionary")
        verbose_name_plural = _(u"Dictionaries")

    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN, verbose_name=_("Item name"))
    active = models.BooleanField(verbose_name=_("Active"), help_text=_("If true this record can be added to new entities"), default=True)
    type = models.CharField(max_length=CHAR_FIELD_MAX_LEN, choices=settings.DICTIONARY_CHOICES)

    def __unicode__(self):
        return ' '.join(('+' if self.active else '-', self.name, self.type))