from rest_framework import serializers
from ..models import BaseDeviation


class BaseDeviationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseDeviation
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        if data['system'] == self.Meta.model.HOLE_SYSTEM:
            data['designation'] = data['designation'].upper()
            data['base_deviation'] = data['base_deviation'].upper()
        return data

    def validate(self, attrs):
        validated_data = super().validate(attrs=attrs)
        validated_data['designation'] = validated_data['designation'].lower()
        validated_data['base_deviation'] = validated_data['base_deviation'].lower()
        return validated_data
