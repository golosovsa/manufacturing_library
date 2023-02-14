from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from common.fields import LowerCaseCharField


class BaseDeviation(models.Model):
    SHAFT_SYSTEM = 'shaft'
    HOLE_SYSTEM = 'hole'
    SYSTEM_CHOICES = [(SHAFT_SYSTEM, _('Shaft system')), (HOLE_SYSTEM, _('Hole system'))]

    DEVIATION_ES = 'es'
    DEVIATION_EI = 'ei'

    DEVIATION_CHOICES = [
        (DEVIATION_ES, _(f'Upper deviation')),
        (DEVIATION_EI, _(f'Lower deviation')),
    ]

    system = models.CharField(max_length=5, null=False, choices=SYSTEM_CHOICES, verbose_name=_('System'))
    base_deviation = models.CharField(max_length=2, null=False, choices=DEVIATION_CHOICES,
                                      verbose_name=_('Base deviation'))
    designation = LowerCaseCharField(max_length=2, null=False, blank=False,
                                     validators=[RegexValidator(regex=r'^[a-zA-Z][a-zA-Z]?$'), ],
                                     verbose_name=_('Designation'))

    class Meta:
        unique_together = ["system", "designation", ]
        verbose_name = _('Base deviation1')
        verbose_name_plural = _('Base deviations')

    def __str__(self):
        designation_alias = self.designation if self.system == self.SHAFT_SYSTEM else self.designation.upper()
        return f"{designation_alias} ({self.system})"
