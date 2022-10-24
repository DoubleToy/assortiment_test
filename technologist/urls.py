from django.urls import path
from .views import get_operations

urlpatterns = [
    path('operations/', get_operations)
]