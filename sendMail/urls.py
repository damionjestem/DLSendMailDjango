from django.urls import path, include
from . import views
from rest_framework import routers

ROUTER = routers.DefaultRouter()
ROUTER.register('sendMails', views.MailView)

urlpatterns = [
    path('', include(ROUTER.urls))
]