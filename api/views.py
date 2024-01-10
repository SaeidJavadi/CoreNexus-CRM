from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsCommonOrReadOnly, IsSuperUser, IsOwnerOrReadOnlyMSG, IsUserOwenerOrReadOnly, \
    NotAllowAction, IsOwnerOrReadOnlyTable
from django.contrib.auth import get_user_model
from crm import models as crmmod
from api import serializers
import json
from django.core.exceptions import ValidationError
from django.db import IntegrityError


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


class AmoountsViewSet(ModelViewSet):
    queryset = crmmod.CommonsAmount.objects.all()
    serializer_class = serializers.AmoountsSerilizer
    filterset_fields = ['name', 'title']
    ordering_fields = ['name', 'title']
    ordering = ['id']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsSuperUser,)
        return [permission() for permission in permission_classes]


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

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        try:
            lottery = self.request.data.get('lottery')
            if lottery == 2:
                amount = crmmod.CommonsAmount.objects.get(name='c60z').id
            else:
                amount = crmmod.CommonsAmount.objects.get(name='c60').id
            data['amount'] = amount
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=400)

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

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        try:
            data = request.data
            amount = crmmod.CommonsAmount.objects.get(name='c61').id
            data['amount'] = amount
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=400)

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

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        try:
            data = request.data
            amount = crmmod.CommonsAmount.objects.get(name='c70').id
            data['amount'] = amount
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=400)

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

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        try:
            data = request.data
            amount = crmmod.CommonsAmount.objects.get(name='cd').id
            data['amount'] = amount
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=400)

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

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        try:
            data = request.data
            amount = crmmod.CommonsAmount.objects.get(name='jd').id
            data['amount'] = amount
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=400)

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

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        try:
            data = request.data
            amount = crmmod.CommonsAmount.objects.get(name='dd').id
            data['amount'] = amount
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=400)

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

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        try:
            data = request.data
            amount = crmmod.CommonsAmount.objects.get(name='pa').id
            data['amount'] = amount
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=400)

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
            if type(updateData['see']) is str:
                updateSee = json.loads(updateData['see'])
            else:
                updateSee = updateData['see']
            if not type(updateSee) is dict:
                raise ValueError('Type Note Allowed for update see')
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
            serializer = self.get_serializer(notificationInstanse, data=updateData,  partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(self.get_serializer(notificationInstanse).data)
            return Response({'message': 'Error to Update.', 'error': serializer.errors}, 400)
        except Exception as e:
            return Response({'message': 'Error to Update.', 'error': 'serializer data'}, 400)


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
        try:
            c60 = crmmod.Common60.objects.get(usersubmit=user)
            queryset = crmmod.WinnerLottery60.objects.filter(common=c60)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response([])


class TableGiftViewSet(ModelViewSet):
    serializer_class = serializers.TableGiftSerializer
    queryset = crmmod.TableGift.objects.all()
    filterset_fields = ['tabletype__name', 'tabletype__id']
    search_fields = ['gifts', 'tabletype__name']
    ordering_fields = ['id',]

    def get_permissions(self):
        if self.action != 'list':
            permission_classes = (NotAllowAction,)
        else:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]


class TabGiftUsrViewSet(ModelViewSet):
    serializer_class = serializers.TableGiftUsrSerializer
    queryset = crmmod.TableGiftUser.objects.all()
    ordering_fields = ['id',]

    # def create(self, request, *args, **kwargs):
    #     return super().create(*args, **kwargs)

    def perform_create(self, serializer):
        try:
            countpay = int(self.request.data.get('countpay'))
            pktabgift = int(self.request.data.get('tablegift'))
            cchances = int(self.request.data.get('countchances'))
            amountpay = crmmod.TableGift.objects.get(id=pktabgift).amount
            if not cchances:
                cchances = 1
            amountpay = amountpay * cchances
            tbcrusr = serializer.save(user=self.request.user, amount=amountpay)
            amountpay = round(amountpay / countpay, 3)
            for i in range(0, countpay):
                py = crmmod.TablePayment.objects.create(tabgiftusr=tbcrusr, payment=amountpay)
            return tbcrusr
        except Exception as e:
            print(e)

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            permission_classes = (NotAllowAction,)
        else:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.TableGiftUser.objects.all()
        else:
            return crmmod.TableGiftUser.objects.filter(user=user)


class TabPayViewSet(ModelViewSet):
    serializer_class = serializers.TablePaySerilizer
    queryset = crmmod.TablePayment.objects.all()
    filterset_fields = ['tabgiftusr__id', 'tabgiftusr__user']
    ordering_fields = ['id',]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsOwnerOrReadOnlyTable,)
        else:
            permission_classes = (IsSuperUser,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.TablePayment.objects.all()
        else:
            return crmmod.TablePayment.objects.filter(tabgiftusr__user__id=user.id)


class TabWinnerViewSet(ModelViewSet):
    serializer_class = serializers.TableWinnerSerilizer
    queryset = crmmod.WinTableLottery.objects.all()
    filterset_fields = ['tabgiftusr__id', 'tabgiftusr__user']
    ordering_fields = ['id',]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsOwnerOrReadOnlyTable,)
        else:
            permission_classes = (IsSuperUser,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return crmmod.WinTableLottery.objects.all()
        else:
            return crmmod.WinTableLottery.objects.filter(tabgiftusr__user__id=user.id)


class SocialMediaViewSet(ModelViewSet):
    serializer_class = serializers.SocialMediaSerilizer
    queryset = crmmod.SocialMedia.objects.filter(active=True)
    filrerset_fields = ['mediatype', 'adv']
    ordering_fields = ['id',]
    ordering = ['-id',]
    http_method_names = ['get',]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsSuperUser,)
        return [permission() for permission in permission_classes]


class ViewPostViewSet(ModelViewSet):
    serializer_class = serializers.ViewPostSerilizer
    queryset = crmmod.ViewPost.objects.all()
    filterset_fields = ['user__username', 'socialmedia__mediatype']
    ordering = ['-id',]
    http_method_names = ['get', 'post',]

    def get_permissions(self):
        if self.action in ['create',]:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsSuperUser,)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        try:
            post_id = int(self.request.data.get('socialmedia'))
            sm = crmmod.SocialMedia.objects.get(id=post_id)
            ser = serializer.save(user=self.request.user, socialmedia=sm)
            p = crmmod.ViewPost.objects.create(user=self.request.user, socialmedia=sm)
            return ser
        except Exception as e:
            print('Error:', e)


class LikePostViewSet(ModelViewSet):
    serializer_class = serializers.LikePostSerilizer
    queryset = crmmod.LikePost.objects.all()
    filterset_fields = ['user__username', 'socialmedia__mediatype']
    ordering = ['-id',]
    http_method_names = ['get', 'post',]

    def get_permissions(self):
        if self.action in ['create',]:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsSuperUser,)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        try:
            post_id = int(self.request.data.get('socialmedia'))
            sm = crmmod.SocialMedia.objects.get(id=post_id)
            ser = serializer.save(user=self.request.user, socialmedia=sm)
            p = crmmod.LikePost.objects.create(user=self.request.user, socialmedia=sm)
            return ser
        except Exception as e:
            print('Error:', e)


class NewsTextViewSet(ModelViewSet):
    serializer_class = serializers.NewsTextSerilizer
    queryset = crmmod.NewsText.objects.filter(active=True)
    ordering = ['-id',]
    http_method_names = ['get', 'post',]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsSuperUser,)
        return [permission() for permission in permission_classes]


class CommentPostViewSet(ModelViewSet):
    serializer_class = serializers.CommentPostSerilizer
    queryset = crmmod.CommentPost.objects.filter(active=True)
    ordering = ['-id',]
    http_method_names = ['get','post']

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create']:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsSuperUser,)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        try:
            post_id = int(self.request.data.get('socialmedia'))
            sm = crmmod.SocialMedia.objects.get(id=post_id)
            ser = serializer.save(user=self.request.user, socialmedia=sm)
            p = crmmod.CommentPost.objects.create(user=self.request.user, socialmedia=sm)
            return ser
        except Exception as e:
            print('Error:', e)
