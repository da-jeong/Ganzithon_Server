# travelapp/urls.py
from django.contrib import admin
from django.urls import path, include
from travelapp.views import city_list
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('city_list/', views.city_list, name="city_list"),
    # 다른 URL 패턴이 필요하면 추가할 수 있습니다.
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)