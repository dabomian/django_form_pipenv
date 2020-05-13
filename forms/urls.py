from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('form1', views.Form1View.as_view(), name='form1'),
]