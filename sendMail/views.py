from django.shortcuts import render
from rest_framework import viewsets
from .models import sendMail
from .serializers import MailSerializer


class MailView(viewsets.ModelViewSet):
    queryset = sendMail.objects.all()
    serializer_class = MailSerializer