from rest_framework import serializers
from django.contrib.auth import get_user_model    # from accounts.models import User
from crm.models import Common60, Common61, Common70, CommonDead, DoingDead, JudiciaryDead, PublicAssistance, \
    Notification, WinnerLottery60, TableGift, TableGiftUser, TablePayment, WinTableLottery, CommonsAmount, SocialMedia, ViewPost, LikePost, NewsText, CommentPost
from drf_dynamic_fields import DynamicFieldsMixin  # GET api/articels/?fields=id,title : show just fields => id,title


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'phone', 'email',
                  'regdate', 'updated', 'last_login', 'is_active', 'is_staff', 'fcmtoken')


class UserSerializerReg(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'phone', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self, request):
        try:
            Phone = self.validated_data['phone']
        except:
            Phone = None
        try:
            Email = self.validated_data['email']
        except:
            Email = None

        user = get_user_model()(
            username=self.validated_data['username'],
            phone=Phone,
            email=Email
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class AmoountsSerilizer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = CommonsAmount
        fields = '__all__'


class Common60Serializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Common60
        fields = '__all__'


class Common61Serializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Common61
        fields = '__all__'


class Common70Serializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Common70
        fields = '__all__'


class CommonDeadSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = CommonDead
        fields = '__all__'


class DoingDeadSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = DoingDead
        fields = '__all__'


class JudiciaryDeadSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = JudiciaryDead
        fields = '__all__'


class PublicAssistanceSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = PublicAssistance
        fields = '__all__'


class NotificationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Notification
        # fields = '__all__'
        exclude = ('user', 'see', 'seedate')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        seelist = instance.see
        username = self.context['request'].user
        user_id = self.context['request'].user.id
        seestatus = False
        if len(seelist) > 0:
            for u, i in seelist.items():
                if str(username) == str(u) and int(user_id) == int(i):
                    seestatus = True
                    break
        representation['see_user'] = seestatus
        return representation


class WinnerLottery60Serializer(DynamicFieldsMixin, serializers.ModelSerializer):
    lottery = serializers.SerializerMethodField('get_lottery')
    common = serializers.SerializerMethodField('get_common')

    def get_lottery(self, obj):
        try:
            return {
                'lottery_title': obj.lottery.title,
            }
        except:
            return None

    def get_common(self, obj):
        try:
            return {
                'id': obj.common.id,
                'name': obj.common.name,
            }
        except:
            return None

    class Meta:
        model = WinnerLottery60
        fields = '__all__'
        # depth = 1


class TableGiftSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    # TablePayment = TabaleNameSerializer()

    class Meta:
        model = TableGift
        fields = '__all__'
        depth = 1


class TableGiftUsrSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = TableGiftUser
        # fields = '__all__'
        exclude = ('paystatus', 'amount', 'updated')


class TbGtSerilizer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = TableGift
        fields = ('gifts',)


class TbGtUsrSerilizer(DynamicFieldsMixin, serializers.ModelSerializer):
    tablegift = TbGtSerilizer()

    class Meta:
        model = TableGiftUser
        fields = ('tablegift',)


class TablePaySerilizer(DynamicFieldsMixin, serializers.ModelSerializer):
    tabgiftusr = TbGtUsrSerilizer()

    class Meta:
        model = TablePayment
        fields = '__all__'
        # depth = 2


class TableWinnerSerilizer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = WinTableLottery
        fields = '__all__'


class SocialMediaSerilizer(DynamicFieldsMixin, serializers.ModelSerializer):
    detail = serializers.SerializerMethodField('get_detail')

    def get_detail(self, obj):
        try:
            views = obj.viewpost.get(user__id=self.context['request'].user.id)
            if views:
                view_status = True
        except:
            view_status = False
        try:
            likes = obj.likepost.get(user__id=self.context['request'].user.id)
            if likes:
                like_status = likes.id
        except:
            like_status = 0
        try:
            return {
                'viewstatus': view_status,
                'views': len(obj.viewpost.all()),
                'likestatus': like_status,
                'likes': len(obj.likepost.all())
            }
        except:
            return None

    class Meta:
        model = SocialMedia
        fields = ('id', 'mediatype', 'file', 'caption', 'detail', 'createdate', 'adv')


class ViewPostSerilizer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = ViewPost
        fields = '__all__'


class LikePostSerilizer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = '__all__'


class NewsTextSerilizer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = NewsText
        fields = ('id', 'text', 'createdt')


class CommentPostSerilizer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        # fields = '__all__'
        exclude = ('updatedt',)
