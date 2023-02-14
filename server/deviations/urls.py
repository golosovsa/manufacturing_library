from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BaseDeviationViewSet, GradeRangeViewSet

router = DefaultRouter()
router.register('base', BaseDeviationViewSet, basename='base-deviation')
router.register('range', GradeRangeViewSet, basename='range-deviation')

urlpatterns = [
    path('', include(router.urls))
]
