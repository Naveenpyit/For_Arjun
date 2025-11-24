from rest_framework.serializers import ModelSerializer
from . import models

class TaskSerializer(ModelSerializer):
    class Meta:
        model = models.TaskModel
        fields = '__all__'