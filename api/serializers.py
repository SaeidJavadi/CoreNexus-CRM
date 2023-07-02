from rest_framework import serializers
from accounts.models import User
from drf_dynamic_fields import DynamicFieldsMixin  # GET api/articels/?fields=id,title : show just fields => id,title


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


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
