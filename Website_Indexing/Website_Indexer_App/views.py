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

    all_pages = models.ParentPage.objects.all()

    for i in all_pages:
        i.child = models.ChildPage.objects.filter(page_name__id = i.id)

    return render(request, "Website_Indexer_App/index.html", context={'all_pages': all_pages})

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

        parent = models.ParentPage.objects.create(search_word=val, title = driver.title)
        for l in links:
            driver.get(l)
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

            all_media = []
            os.chdir(settings.MEDIA_ROOT)
            for i in img:
                src = i.get_attribute('src')
                media_name = src.split('/')[-1]
                all_media.append(media_name)
                # download the image
                urllib.request.urlretrieve(src, media_name)
            models.ChildPage.objects.create(
                page_name=parent, url=l, title=title, keywords=keywords, media=all_media)

            # driver.close()
        driver.quit()
        return JsonResponse(1,safe=False)
    else:
        return JsonResponse(0,safe=False)
