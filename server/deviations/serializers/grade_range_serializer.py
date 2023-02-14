from rest_framework import serializers
from ..models import GradeRange


class GradeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeRange
        fields = "__all__"
