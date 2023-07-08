from rest_framework import serializers

from django.contrib.auth import get_user_model    # from accounts.models import User
from crm.models import Common60, Common61, Common70, CommonDead, DoingDead, JudiciaryDead, PublicAssistance
from drf_dynamic_fields import DynamicFieldsMixin  # GET api/articels/?fields=id,title : show just fields => id,title


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class UserNestedSerilizer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class UserSerializerReg(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

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
        # password2 = self.validated_data['password2']

        # if password != password2:
        #     raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class Common60Serializer(DynamicFieldsMixin, serializers.ModelSerializer):
    # usersubmit = serializers.SerializerMethodField("get_usersubmit")
    usersubmit = UserNestedSerilizer()

    class Meta:
        model = Common60
        fields = '__all__'

    # def get_usersubmit(self, obj):
    #     try:
    #         return {
    #             "user_id": obj.usersubmit.id,
    #             "username": obj.usersubmit.username
    #         }
    #     except:
    #         return None


class Common61Serializer(DynamicFieldsMixin, serializers.ModelSerializer):
    usersubmit = serializers.SerializerMethodField("get_usersubmit")

    class Meta:
        model = Common61
        fields = '__all__'

    def get_usersubmit(self, obj):
        try:
            return {
                "user_id": obj.usersubmit.id,
                "username": obj.usersubmit.username
            }
        except:
            return None


class Common70Serializer(DynamicFieldsMixin, serializers.ModelSerializer):
    usersubmit = serializers.SerializerMethodField("get_usersubmit")

    class Meta:
        model = Common70
        fields = '__all__'

    def get_usersubmit(self, obj):
        try:
            return {
                "user_id": obj.usersubmit.id,
                "username": obj.usersubmit.username
            }
        except:
            return None


class CommonDeadSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    usersubmit = serializers.SerializerMethodField("get_usersubmit")

    class Meta:
        model = CommonDead
        fields = '__all__'

    def get_usersubmit(self, obj):
        try:
            return {
                "user_id": obj.usersubmit.id,
                "username": obj.usersubmit.username
            }
        except:
            return None


class DoingDeadSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    usersubmit = serializers.SerializerMethodField("get_usersubmit")

    class Meta:
        model = DoingDead
        fields = '__all__'

    def get_usersubmit(self, obj):
        try:
            return {
                "user_id": obj.usersubmit.id,
                "username": obj.usersubmit.username
            }
        except:
            return None


class JudiciaryDeadSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    usersubmit = serializers.SerializerMethodField("get_usersubmit")

    class Meta:
        model = JudiciaryDead
        fields = '__all__'

    def get_usersubmit(self, obj):
        try:
            return {
                "user_id": obj.usersubmit.id,
                "username": obj.usersubmit.username
            }
        except:
            return None


class PublicAssistanceSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    usersubmit = serializers.SerializerMethodField("get_usersubmit")

    class Meta:
        model = PublicAssistance
        fields = '__all__'

    def get_usersubmit(self, obj):
        try:
            return {
                "user_id": obj.usersubmit.id,
                "username": obj.usersubmit.username
            }
        except:
            return None


# class WorkerSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
#     # server = ServerSerilizer()
#     task = serializers.SerializerMethodField("get_task")
#     server = serializers.SerializerMethodField("get_server")
#     number = serializers.SerializerMethodField("get_number")

#     class Meta:
#         model = Worker
#         fields = ('id', 'done', 'status', 'task', 'server', 'number')

#     def get_server(self, obj):
#         try:
#             return {
#                 "ip": obj.usersubmit.server.ip,
#                 "status": obj.usersubmit.server.status,
#             }
#         except:
#             return None

#     def get_task(self, obj):
#         try:
#             return {
#                 "id": obj.usersubmit.task.id,
#                 "action": obj.usersubmit.task.action,
#                 # "text": obj.usersubmit.task.text,
#                 # "image": str(obj.usersubmit.task.image),
#                 # "delay": obj.usersubmit.task.delay,
#                 "status": obj.usersubmit.task.status,
#             }
#         except:
#             return None

#     def get_number(self, obj):
#         try:
#             return {
#                 "id": obj.usersubmit.number.id,
#                 "number": obj.usersubmit.number.num,
#                 "status": obj.usersubmit.number.status,
#                 "checkit": obj.usersubmit.number.checkit
#             }
#         except:
#             return None
