from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('process_data/', views.process_data, name="process_data"),
]
