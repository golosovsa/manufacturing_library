from .mixins import LowerCaseFieldMixin
from django.db import models


class LowerCaseCharField(LowerCaseFieldMixin, models.CharField):
    pass
