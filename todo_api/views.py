from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from mytodos.models import Todo
from .serializers import TodoSerializer


class TodoViewSet(ModelViewSet):
    # http_method_names = ['get', 'post', 'delete']
    queryset = Todo.objects.order_by("-created")
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}
