from django.shortcuts import render
from django.views.generic import TemplateView #
# Create your views here.
'''from django.http import HttpResponse
def  TestView(request, **kwargs):
	return HttpResponse("Hello Word")'''

from mongoengine import *
#connect("datascience")
from models import Poll
poll = Poll(question="What is your name", )
poll.save()

#print poll.question
class SplashView(TemplateView):
	template_name = "index.html" 