from django.urls import path
from accounts import views
from django.contrib.auth.decorators import login_required


app_name = 'accounts'
urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('register/', views.userRegister, name='register'),
    path('logout/', views.LogoutPage, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/change/password', views.profilepass, name='profilepass'),
    path('users/', login_required(views.UsersListView.as_view()), name='user_list'),
    path('users/create', login_required(views.UserCreateView.as_view()), name='user_create'),
    path('users/detail/<int:pk>', login_required(views.UserDetailView.as_view()), name='user_detail'),
    path('users/update/<int:pk>', login_required(views.UsersUpdateView.as_view()), name='user_update'),
    path('users/update/password/<int:pk>', login_required(views.UsersUpdatePassView.as_view()), name='user_updatepassword'),
    path('users/delete/<int:pk>', login_required(views.UsersDeleteView.as_view()), name='user_delete'),
]
