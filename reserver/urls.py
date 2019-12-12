from django.urls import path
from .views import Top

app_name = 'reserver'

urlpatterns = [
    path('top/', Top.as_view(), name='top'),
]
