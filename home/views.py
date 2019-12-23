from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def home():
	
	return ""
