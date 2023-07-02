from django.urls import path
from api.views import UserList, UsereDetail

app_name = "api"

urlpatterns = [
    path("users/", UserList.as_view(), name="userlist"),
    path("users/<int:pk>", UsereDetail.as_view(), name="userdetail"),
 
]
