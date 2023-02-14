from django.contrib import admin

# Register your models here.
from .models import BaseDeviation, BaseDeviationGrade, GradeRange

admin.site.register(BaseDeviation)
admin.site.register(BaseDeviationGrade)
admin.site.register(GradeRange)
