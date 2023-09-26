from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    return HttpResponse('sucessfully installed data....')

def insert_webpage(request):
    return HttpResponse('sucessfully inserted')

def insert_acessrecords(request):
    return HttpResponse('data sucessfully inserted')