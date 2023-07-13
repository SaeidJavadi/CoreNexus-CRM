from django.urls import path
from crm import views
from django.contrib.auth.decorators import login_required

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('c60/', login_required(views.C60List.as_view()), name='c60list')
]
