from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import redis

# Create your views here.

def index(request):
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	r.set('foo','rob')
	template = loader.get_template('index.html')
	return HttpResponse(template.render()) #render(request,"index.html",content_type='text/html')
