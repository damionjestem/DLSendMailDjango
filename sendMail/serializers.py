from rest_framework import serializers
from .models import sendMail

class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = sendMail
        fields = ('id', 'email', 'rss')