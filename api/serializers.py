from rest_framework import serializers
from accounts.models import User
from drf_dynamic_fields import DynamicFieldsMixin  # GET api/articels/?fields=id,title : show just fields => id,title


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSerializerReg(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
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

        user = User(
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
#                 "ip": obj.server.ip,
#                 "status": obj.server.status,
#             }
#         except:
#             return None

#     def get_task(self, obj):
#         try:
#             return {
#                 "id": obj.task.id,
#                 "action": obj.task.action,
#                 # "text": obj.task.text,
#                 # "image": str(obj.task.image),
#                 # "delay": obj.task.delay,
#                 "status": obj.task.status,
#             }
#         except:
#             return None

#     def get_number(self, obj):
#         try:
#             return {
#                 "id": obj.number.id,
#                 "number": obj.number.num,
#                 "status": obj.number.status,
#                 "checkit": obj.number.checkit
#             }
#         except:
#             return None
