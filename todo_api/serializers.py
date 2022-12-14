from rest_framework import serializers
from mytodos.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['id', 'title', 'created', "updated", "completed"]
