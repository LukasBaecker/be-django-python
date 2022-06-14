import coreapi
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.schemas import AutoSchema
from rest_framework.parsers import JSONParser

from .models import Recipient
from .serializers import NewsletterSerializer


class NewsletterViewSchema(AutoSchema):
     
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    name = 'name',
                    required = False,
                    description= 'Name of the Newsletter-Recipient',
                    type='string'), 
                coreapi.Field(
                    name = 'email',
                    required = True,
                    description= 'Email-Address of the Newsletter-Recipient',
                    type='string'),  
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

# Create your views here.
class NewsletterView(APIView):
    schema =NewsletterViewSchema()
    def get(self,request):
       if request.method == 'GET':
        recipients = Recipient.objects.all()
        newsletter_serializer = NewsletterSerializer(recipients, many=True)
        return JsonResponse(newsletter_serializer.data, safe=False)

class NewsletterViewPost(APIView):
    schema =NewsletterViewSchema()

    def post(self,request):  
        newsletter_data = JSONParser().parse(request) 
        newsletter_serializer = NewsletterSerializer(data=newsletter_data) 
        if newsletter_serializer.is_valid(): 
            newsletter_serializer.save() 
            return JsonResponse(newsletter_serializer.data, status=status.HTTP_201_CREATED) 
        else:
            queryset = Recipient.objects.filter(email=newsletter_data['email'])
            if queryset.exists():
                return JsonResponse(newsletter_serializer.errors, status=status.HTTP_303_SEE_OTHER) 
            else:
                return JsonResponse(newsletter_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 