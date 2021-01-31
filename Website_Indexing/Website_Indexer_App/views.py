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
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get(val)
        social = [
            'facebook.com',
            'instagram.com',
            'twitter.com',
            'linkedin.com',
            'pinterest.com',
            'youtube.com',
            'flipboard.com',
            'google.com',
            'reddit.com',
            '@'
        ]
        links = []
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            temp_link = elem.get_attribute("href")
            if [i for i in social if
                i in temp_link or re.match(".*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?", str(temp_link))]:
                pass
            else:
                links.append(temp_link)

        links = list(set(links))
        for l in links:
            meta_desc_list = driver.find_elements_by_xpath("//meta[@name='description']")
            meta_desc = None
            for desc in meta_desc_list:
                meta_desc = desc.get_attribute("content")

            title = driver.title

            keywords_list = driver.find_elements_by_xpath("//meta[@name='keywords']")
            keywords = None
            for keyword in keywords_list:
                keywords = keyword.get_attribute("content")

            img = driver.find_elements_by_tag_name('img')


            folder_name = str(settings.MEDIA_ROOT)
            os.chdir(settings.MEDIA_ROOT)
            # os.mkdir(folder_name)
            # os.chdir(folder_name)
            for i in img:
                src = i.get_attribute('src')

                # download the image
                urllib.request.urlretrieve(src, src.split('/')[-1])
                break
            break
        driver.quit()
        return JsonResponse([settings.STATIC_ROOT, settings.MEDIA_ROOT],safe=False)
    else:
        return JsonResponse([0],safe=False)
