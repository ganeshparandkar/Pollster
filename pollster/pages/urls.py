from django.urls import path,include

from . import views


urlpatterns = [
    path('', views.index, name = 'index'),

    #we are passing id from details class
]
