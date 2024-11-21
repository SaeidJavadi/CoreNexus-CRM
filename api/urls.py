from django.urls import path, include
from api import views
from rest_framework import routers

app_name = 'api'
router = routers.SimpleRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('amounts', views.AmoountsViewSet, basename='amounts')
router.register('c60', views.Common60ViewSet, basename='Common60')
router.register('c61', views.Common61ViewSet, basename='Common61')
router.register('c70', views.Common70ViewSet, basename='Common70')
router.register('cd', views.CommonDeadViewSet, basename='CommonDead')
router.register('jd', views.JudiciaryDeadViewSet, basename='JudiciaryDead')
router.register('dd', views.DoingDeadViewSet, basename='DoingDead')
router.register('pa', views.PublicAssistanceViewSet, basename='PublicAssistance')
router.register('msg', views.NotificationViewSet, basename='Notification')
router.register('lotteryc60', views.LotteryListView, basename='lotteryapi')
router.register('tabsgift', views.TableGiftViewSet, basename='tablegift')
router.register('tabgiftusr', views.TabGiftUsrViewSet, basename='tabgiftusr')
router.register('tabpay', views.TabPayViewSet, basename='tabpay')
router.register('tabwinner', views.TabWinnerViewSet, basename='tabwin')
router.register('socialmedia', views.SocialMediaViewSet, basename='socialmedia')
router.register('view', views.ViewPostViewSet, basename='view')
router.register('like', views.LikePostViewSet, basename='like')
router.register('comment', views.CommentPostViewSet, basename='comment')
router.register('newstext', views.NewsTextViewSet, basename='newstext')

urlpatterns = [
    path('', include(router.urls)),
    path('user/revoke/', views.RevokeToken.as_view(), name='revoketoken')
]
