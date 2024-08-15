from django.urls import path
from .views import DataAPIView

urlpatterns = [
    path('data/', DataAPIView.as_view())
]