from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

from .base_deviation import BaseDeviation
from .grade_range import GradeRange


class BaseDeviationGrade(models.Model):
    range = models.ForeignKey(to=GradeRange, null=False, on_delete=models.CASCADE, verbose_name=_('Grade range'))
    base_deviation = models.ForeignKey(to=BaseDeviation, null=False, on_delete=models.CASCADE,
                                       verbose_name=_('Base deviation'))
    value_um = models.IntegerField()

    class Meta:
        unique_together = ['range', 'base_deviation']
        verbose_name = _('Base deviation grade')
        verbose_name_plural = _('Base deviation grades')
