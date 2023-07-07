from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.permissions import IsCommonOrReadOnly, IsSuperUser, IsSuperUserOrStaffReadOnly
from django.contrib.auth import get_user_model
from crm import models as crmmod
from api import serializers


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        return Response({"msg": "Token Revoked."})


class Common60ViewSet(ModelViewSet):
    serializer_class = serializers.Common60Serializer
    filterset_fields = ["status", "author"]
    ordering_fields = ["create", "status"]
    ordering = ["-create"]
    search_fields = [
        "title",
        "content",
        "author__username",
        "author__first_name",
        "author__last_name"
    ]

    def get_permissions(self):
        if self.action in ['create', ]:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsCommonOrReadOnly,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.Common60.objects.all()
        else:
            return crmmod.Common60.objects.filter(usersubmit=user)


class Common61ViewSet(ModelViewSet):
    serializer_class = serializers.Common61Serializer
    filterset_fields = ["status", "author"]
    ordering_fields = ["create", "status"]
    ordering = ["-create"]
    search_fields = [
        "title",
        "content",
        "author__username",
        "author__first_name",
        "author__last_name"
    ]

    def get_permissions(self):
        if self.action in ['create', ]:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsCommonOrReadOnly,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.Common61.objects.all()
        else:
            return crmmod.Common61.objects.filter(usersubmit=user)


class Common70ViewSet(ModelViewSet):
    serializer_class = serializers.Common70Serializer
    filterset_fields = ["status", "author"]
    ordering_fields = ["create", "status"]
    ordering = ["-create"]
    search_fields = [
        "title",
        "content",
        "author__username",
        "author__first_name",
        "author__last_name"
    ]

    def get_permissions(self):
        if self.action in ['create', ]:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsCommonOrReadOnly,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.Common70.objects.all()
        else:
            return crmmod.Common70.objects.filter(usersubmit=user)


class CommonDeadViewSet(ModelViewSet):
    serializer_class = serializers.CommonDeadSerializer
    filterset_fields = ["status", "author"]
    ordering_fields = ["create", "status"]
    ordering = ["-create"]
    search_fields = [
        "title",
        "content",
        "author__username",
        "author__first_name",
        "author__last_name"
    ]

    def get_permissions(self):
        if self.action in ['create', ]:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsCommonOrReadOnly,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.CommonDead.objects.all()
        else:
            return crmmod.CommonDead.objects.filter(usersubmit=user)


class JudiciaryDeadViewSet(ModelViewSet):
    serializer_class = serializers.JudiciaryDeadSerializer
    filterset_fields = ["status", "author"]
    ordering_fields = ["create", "status"]
    ordering = ["-create"]
    search_fields = [
        "title",
        "content",
        "author__username",
        "author__first_name",
        "author__last_name"
    ]

    def get_permissions(self):
        if self.action in ['create', ]:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsCommonOrReadOnly,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.JudiciaryDead.objects.all()
        else:
            return crmmod.JudiciaryDead.objects.filter(usersubmit=user)


class DoingDeadViewSet(ModelViewSet):
    serializer_class = serializers.DoingDeadSerializer
    filterset_fields = ["status", "author"]
    ordering_fields = ["create", "status"]
    ordering = ["-create"]
    search_fields = [
        "title",
        "content",
        "author__username",
        "author__first_name",
        "author__last_name"
    ]

    def get_permissions(self):
        if self.action in ['create', ]:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsCommonOrReadOnly,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.DoingDead.objects.all()
        else:
            return crmmod.DoingDead.objects.filter(usersubmit=user)


class PublicAssistanceViewSet(ModelViewSet):
    serializer_class = serializers.PublicAssistanceSerializer
    filterset_fields = ["status", "author"]
    ordering_fields = ["create", "status"]
    ordering = ["-create"]
    search_fields = [
        "title",
        "content",
        "author__username",
        "author__first_name",
        "author__last_name"
    ]

    def get_permissions(self):
        if self.action in ['create', ]:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsCommonOrReadOnly,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.PublicAssistance.objects.all()
        else:
            return crmmod.PublicAssistance.objects.filter(usersubmit=user)


