from django.urls import path
from crm import views

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
]
