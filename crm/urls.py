from django.urls import path
from crm import views
from django.contrib.auth.decorators import login_required

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('c60/', login_required(views.C60List.as_view()), name='c60list'),
    path('c60/filter/', views.ObjFilterView.as_view(), name='filter_obj'),
    path('c60/create/', views.ObjCreateView.as_view(), name='create_obj'),
    path('c60/update/<int:pk>', views.ObjUpdateView.as_view(), name='update_obj'),
    path('c60/read/<int:pk>', views.ObjReadView.as_view(), name='read_obj'),
    path('c60/delete/<int:pk>', views.ObjDeleteView.as_view(), name='delete_obj'),
    path('c60/objs/', views.objs, name='objs'),
]
