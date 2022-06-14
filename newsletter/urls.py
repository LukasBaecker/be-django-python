from django.contrib import admin
from django.urls import path
from . import views
from newsletter.views import * 
from newsletter import views 

#URLConf
urlpatterns = [
    path('all/', NewsletterView.as_view()),
    path('', NewsletterViewPost.as_view()),
]
