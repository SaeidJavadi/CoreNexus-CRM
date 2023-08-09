from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.permissions import IsCommonOrReadOnly, IsSuperUser, IsSuperUserOrStaffReadOnly, IsOwnerOrReadOnlyMSG, IsUserOwenerOrReadOnly
from django.contrib.auth import get_user_model
from crm import models as crmmod
from api import serializers
import json


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    # permission_classes = (IsSuperUserOrStaffReadOnly,)

    def get_permissions(self):
        if self.action in ['get', ]:
            permission_classes = (IsAuthenticated,)
        elif self.action in ['create', 'destroy']:
            permission_classes = (IsSuperUser,)
        else:
            permission_classes = (IsUserOwenerOrReadOnly,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return get_user_model().objects.all()
        elif user.is_authenticated:
            return get_user_model().objects.filter(id=user.id)

    def update(self, request, *args, **kwargs):
        userInstanse = self.get_object()
        updateData = request.data.copy()
        # fcm_token = True if 'fcmtoken' in updateData.keys() else False
        key_to_keep = 'fcmtoken'
        keys_to_remove = []
        for key in updateData.keys():
            if key != key_to_keep:
                keys_to_remove.append(key)
        for key in keys_to_remove:
            updateData.pop(key)
        serializer = serializers.UserSerializer(userInstanse, data=updateData,  partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializers.UserSerializer(userInstanse).data)
        return Response({'message': 'Error to Update.', 'error': serializer.errors}, 400)


class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        return Response({'msg': 'Token Revoked.'})


class Common60ViewSet(ModelViewSet):
    serializer_class = serializers.Common60Serializer
    filterset_fields = ['status', 'usersubmit']
    ordering_fields = ['create', 'status']
    ordering = ['-create']
    search_fields = [
        'name',
        'phone',
        'usersubmit__username',
        'usersubmit__phone',
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
    filterset_fields = ['status', 'usersubmit']
    ordering_fields = ['create', 'status']
    ordering = ['-create']
    search_fields = [
        'name',
        'phone',
        'usersubmit__username',
        'usersubmit__phone',
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
    filterset_fields = ['status', 'usersubmit']
    ordering_fields = ['create', 'status']
    ordering = ['-create']
    search_fields = [
        'name',
        'phone',
        'usersubmit__username',
        'usersubmit__phone',
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
    filterset_fields = ['status', 'usersubmit']
    ordering_fields = ['create', 'status']
    ordering = ['-create']
    search_fields = [
        'name',
        'phone',
        'usersubmit__username',
        'usersubmit__phone',
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
    filterset_fields = ['status', 'usersubmit']
    ordering_fields = ['create', 'status']
    ordering = ['-create']
    search_fields = [
        'name',
        'phone',
        'usersubmit__username',
        'usersubmit__phone',
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
    filterset_fields = ['status', 'usersubmit']
    ordering_fields = ['create', 'status']
    ordering = ['-create']
    search_fields = [
        'name',
        'phone',
        'usersubmit__username',
        'usersubmit__phone',
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
    filterset_fields = ['status', 'usersubmit']
    ordering_fields = ['create', 'status']
    ordering = ['-create']
    search_fields = [
        'help_name',
        'amount',
        'usersubmit__username',
        'usersubmit__phone',
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


class NotificationViewSet(ModelViewSet):
    serializer_class = serializers.NotificationSerializer
    filterset_fields = ['user',]
    ordering_fields = ['createdate',]
    ordering = ['-createdate']
    search_fields = ['subject', 'text', 'user__username', 'user__email', 'user__phone']

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = (IsSuperUser,)
        else:
            permission_classes = (IsOwnerOrReadOnlyMSG,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.Notification.objects.all()
        else:
            return crmmod.Notification.objects.filter(user=user)

    def update(self, request, *args, **kwargs):
        notificationInstanse = self.get_object()
        seeList = notificationInstanse.see
        updateData = request.data.copy()
        try:
            if not type(seeList) is dict:
                seeList = {}
            updateSee = json.loads(updateData['see'])
            if not type(updateSee) is dict:
                raise ValueError("Type Note Allowed for update see")
            for k, v in updateSee.items():
                seeList[k] = v
            updateData['see'] = seeList
            key_to_keep = 'see'
            keys_to_remove = []
            for key in updateData.keys():
                if key != key_to_keep:
                    keys_to_remove.append(key)
            for key in keys_to_remove:
                updateData.pop(key)
            serializer = serializers.NotificationSerializer(notificationInstanse, data=updateSee,  partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializers.NotificationSerializer(notificationInstanse).data)
            return Response({'message': 'Error to Update.', 'error': serializer.errors}, 400)
        except:
            return Response({'message': 'Error to Update.', 'error': serializer.errors}, 400)


class LotteryListView(ModelViewSet):
    serializer_class = serializers.WinnerLottery60Serializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update']:
            permission_classes = (IsSuperUser,)
        else:
            permission_classes = (IsUserOwenerOrReadOnly,)
        return [permission() for permission in permission_classes]

    def list(self, request):
        user = request.user.id
        c60 = crmmod.Common60.objects.get(usersubmit=user)
        queryset = crmmod.WinnerLottery60.objects.filter(common=c60)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
