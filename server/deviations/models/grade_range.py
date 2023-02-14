from django.core.validators import MinValueValidator
from django.utils.translation import gettext as _
from django.db import models


class GradeRange(models.Model):
    range_over = models.IntegerField(null=False, validators=[MinValueValidator(0), ], verbose_name=_('Over'))
    range_up_to = models.IntegerField(null=False, validators=[MinValueValidator(0), ], verbose_name=_('Up to'))

    class Meta:
        unique_together = ['range_over', 'range_up_to']
        verbose_name = _('Range')
        verbose_name_plural = _('Ranges')

    def __str__(self):
        return _('Over {} up to {}').format(self.range_over, self.range_up_to)
