from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
# from api.permissions import IsClientOrReadOnly
from accounts.models import User
from crm import models as crmmod
from api import serializers


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAdminUser,)


class UsereDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAdminUser,)


class Common60View(ListCreateAPIView):
    queryset = crmmod.Common60.objects.all()
    serializer_class = serializers.Common60Serializer
    permission_classes = (IsAdminUser,)


class Common60ViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.Common60.objects.all()
    serializer_class = serializers.Common60Serializer
    permission_classes = (IsAdminUser,)


class Common61View(ListCreateAPIView):
    queryset = crmmod.Common61.objects.all()
    serializer_class = serializers.Common61Serializer
    permission_classes = (IsAdminUser,)


class Common61ViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.Common61.objects.all()
    serializer_class = serializers.Common61Serializer
    permission_classes = (IsAdminUser,)


class Common70View(ListCreateAPIView):
    queryset = crmmod.Common70.objects.all()
    serializer_class = serializers.Common70Serializer
    permission_classes = (IsAdminUser,)


class Common70ViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.Common70.objects.all()
    serializer_class = serializers.Common70Serializer
    permission_classes = (IsAdminUser,)


class CommonDeadView(ListCreateAPIView):
    queryset = crmmod.CommonDead.objects.all()
    serializer_class = serializers.CommonDeadSerializer
    permission_classes = (IsAdminUser,)


class CommonDeadViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.CommonDead.objects.all()
    serializer_class = serializers.CommonDeadSerializer
    permission_classes = (IsAdminUser,)


class JudiciaryDeadView(ListCreateAPIView):
    queryset = crmmod.JudiciaryDead.objects.all()
    serializer_class = serializers.JudiciaryDeadSerializer
    permission_classes = (IsAdminUser,)


class JudiciaryDeadViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.JudiciaryDead.objects.all()
    serializer_class = serializers.JudiciaryDeadSerializer
    permission_classes = (IsAdminUser,)


class DoingDeadView(ListCreateAPIView):
    queryset = crmmod.DoingDead.objects.all()
    serializer_class = serializers.DoingDeadSerializer
    permission_classes = (IsAdminUser,)


class DoingDeadViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.DoingDead.objects.all()
    serializer_class = serializers.DoingDeadSerializer
    permission_classes = (IsAdminUser,)


class PublicAssistanceView(ListCreateAPIView):
    queryset = crmmod.PublicAssistance.objects.all()
    serializer_class = serializers.PublicAssistanceSerializer
    permission_classes = (IsAdminUser,)


class PublicAssistanceViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.PublicAssistance.objects.all()
    serializer_class = serializers.PublicAssistanceSerializer
    permission_classes = (IsAdminUser,)
