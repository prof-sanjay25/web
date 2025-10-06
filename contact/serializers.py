from rest_framework import serializers
from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            'id', 'name', 'email', 'company', 'phone', 'service', 'message', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


