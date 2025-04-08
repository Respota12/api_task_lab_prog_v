from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'service', ServiceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

