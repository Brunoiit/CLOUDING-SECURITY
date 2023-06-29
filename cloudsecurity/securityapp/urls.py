from django.urls import path
from securityapp.views import scrape

urlpatterns = [
    path('', scrape, name='scrape'),
]