from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	
	return HttpResponse("Hello, world. You're at the polls index.")
