from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "GSM Riders Super Admin Panel"
admin.site.site_title = "GSM Riders Super Admin"


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('Website_Indexer_App.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)