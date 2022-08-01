from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import AllowAny
from mytodos.models import Todo
from .serializers import TodoSerializer


class TodoViewSet(ModelViewSet):
    # http_method_names = ['get', 'post', 'delete']
    queryset = Todo.objects.order_by("-created")
    serializer_class = TodoSerializer

    def get_serializer_context(self):
        return {"request": self.request}


@api_view(["delete"])
def delete_completed(request):
    if request.method == "DELETE":
        Todo.objects.filter(completed=True).delete()
        return Response("Successfully Deleted Completed", status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("method not supported", status=status.HTTP_401_UNAUTHORIZED)


@api_view(["delete"])
def delete_all(request):
    if request.method == "DELETE":
        Todo.objects.all().delete()
        return Response("Successfully Deleted All", status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("method not supported", status=status.HTTP_401_UNAUTHORIZED)
