from django.urls import path
from crm import views

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('c60/', views.C60sListView.as_view(), name='common60'),
    path('c60/create/', views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('c60/delete/', views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('c60/update/', views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
]
