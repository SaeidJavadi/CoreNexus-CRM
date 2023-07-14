from django.urls import path
from crm import views
from django.contrib.auth.decorators import login_required

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('c60/', login_required(views.c60List.as_view()), name='c60_list'),
    path('c60/create/', login_required(views.C60CreateView.as_view()), name='c60_create'),
    path('c60/read/<int:pk>', login_required(views.C60ReadView.as_view()), name='c60_read'),
    path('c60/update/<int:pk>', login_required(views.C60EUpdateView.as_view()), name='c60_update'),
    path('c60/delete/<int:pk>', login_required(views.C60DeleteView.as_view()), name='c60_delete'),
    path('c61/', login_required(views.c61List.as_view()), name='c61_list'),
    path('c61/create/', login_required(views.C61CreateView.as_view()), name='c61_create'),
    path('c61/read/<int:pk>', login_required(views.C61ReadView.as_view()), name='c61_read'),
    path('c61/update/<int:pk>', login_required(views.C61EUpdateView.as_view()), name='c61_update'),
    path('c61/delete/<int:pk>', login_required(views.C61DeleteView.as_view()), name='c61_delete'),
    path('c70/', login_required(views.c70List.as_view()), name='c70_list'),

]
