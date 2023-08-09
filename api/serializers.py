from rest_framework import serializers
from django.contrib.auth import get_user_model    # from accounts.models import User
from crm.models import Common60, Common61, Common70, CommonDead, DoingDead, JudiciaryDead, PublicAssistance, Notification, WinnerLottery60
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
                print(username, user_id)
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
