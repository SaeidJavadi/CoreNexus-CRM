from django.urls import path
from api import views
app_name = "api"

urlpatterns = [
    path("users/", views.UserList.as_view(), name="userlist"),
    path("users/<int:pk>", views.UsereDetail.as_view(), name="userdetail"),
    path("c60/", views.Common60View.as_view(), name="common60"),
    path("c60/<int:pk>", views.Common60ViewDetail.as_view(), name="common60Detail"),
    path("c61/", views.Common61View.as_view(), name="common61"),
    path("c61/<int:pk>", views.Common61ViewDetail.as_view(), name="common61Detail"),
    path("c70/", views.Common70View.as_view(), name="common70"),
    path("c70/<int:pk>", views.Common70ViewDetail.as_view(), name="common70Detail"),
    path("cd/", views.CommonDeadView.as_view(), name="CommonDead"),
    path("cd/<int:pk>", views.CommonDeadViewDetail.as_view(), name="CommonDeadDetail"),
    path("jd/", views.JudiciaryDeadView.as_view(), name="JudiciaryDead"),
    path("jd/<int:pk>", views.JudiciaryDeadViewDetail.as_view(), name="JudiciaryDeadDetail"),
    path("dd/", views.DoingDeadView.as_view(), name="DoingDead"),
    path("dd/<int:pk>", views.DoingDeadViewDetail.as_view(), name="DoingDeadDetail"),
    path("pa/", views.PublicAssistanceView.as_view(), name="PublicAssistanceView"),
    path("pa/<int:pk>", views.PublicAssistanceViewDetail.as_view(), name="PublicAssistanceViewDetail"),

]


