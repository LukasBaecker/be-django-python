from rest_framework import serializers
from newsletter.models import Recipient

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'