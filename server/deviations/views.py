from django.shortcuts import HttpResponse, render
from rest_framework import viewsets, permissions
from .models import BaseDeviation, GradeRange
from .serializers import BaseDeviationSerializer, GradeRangeSerializer


class BaseDeviationViewSet(viewsets.ModelViewSet):
    model = BaseDeviation
    serializer_class = BaseDeviationSerializer
    permission_classes = [permissions.AllowAny, ]
    queryset = model.objects.all()


class GradeRangeViewSet(viewsets.ModelViewSet):
    model = GradeRange
    serializer_class = GradeRangeSerializer
    permission_classes = [permissions.AllowAny, ]
    queryset = model.objects.all()
