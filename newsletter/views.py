import coreapi
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Recipient
from rest_framework.schemas import AutoSchema
from .serializers import NewsletterSerializer
from django.http.response import JsonResponse

class CropViewSchema(AutoSchema):

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
def say_hello(request):
   # return HttpResponse('Hello World')
   return render(request, 'hello.html')


# Create your views here.
class NewsletterView(APIView):
    schema =CropViewSchema()
    def get(self,request):
   
       if request.method == 'GET':
        recipients = Recipient.objects.all()
        crop_serializer = NewsletterSerializer(recipients, many=True)
        return JsonResponse(crop_serializer.data, safe=False)