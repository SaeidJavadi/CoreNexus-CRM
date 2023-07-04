from rest_framework import serializers
from accounts.models import User
from drf_dynamic_fields import DynamicFieldsMixin  # GET api/articels/?fields=id,title : show just fields => id,title


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSerializerReg(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'fullname', 'phone', 'brithday', 'idcode', 'contery',
                  'sickness', 'reagent', 'password', 'password2')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self, request):
        user = User(
            username=self.validated_data['username'],
            fullname=self.validated_data['fullname'],
            phone=self.validated_data['phone'],
            brithday=self.validated_data['brithday'],
            idcode=self.validated_data['idcode'],
            contery=self.validated_data['contery'],
            sickness=self.validated_data['sickness'],
            reagent=self.validated_data['reagent'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


# class TaskSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

#     class Meta:
#         model = Task
#         fields = "__all__"


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
