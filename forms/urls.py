from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.Form1View.as_view(), name='index'),
]