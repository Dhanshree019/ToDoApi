from rest_framework.serializers import ModelSerializer
from .models import ToDoData

class ToDoSerializer(ModelSerializer):

    class Meta:
        model = ToDoData
        fields = "__all__"







