from django.shortcuts import render
from . import models
from django.conf import settings
from selenium import webdriver
import urllib.request
import time
import os
import glob
import re

# Create your views here.
from django.http import JsonResponse, HttpResponse , HttpResponseRedirect

def home_page(request):

    return render(request, "Website_Indexer_App/index.html")

def process_data(request):
    if request.method == 'POST':
        val = request.POST['data']
        return JsonResponse(val,safe=False)
    else:
        return JsonResponse([0],safe=False)
