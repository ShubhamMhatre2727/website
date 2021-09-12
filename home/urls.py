from django.contrib import admin
from django.urls import path
from home import views

from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path("", views.home, name="home"),
    path('gym_workout', views.gym_workout, name="gym_workout")
]

urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)