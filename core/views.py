from requests import Response
from .models import User
from .serializers import UserCreateSerializer

from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class UserAPIView(CreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserCreateSerializer
   # permission_classes = [IsAdminOrReadOnly]
   
   # def post(self, request):
   #    serializer = UserCreateSerializer(data=request.data)
   #    serializer.is_valid(raise_exception=True)
   #    serializer.save()
   #    return Response(status.HTTP_201_CREATED)
   #    # return Response(reg_serializer.errors, status.HTTP_400_BAD_REQUEST)
   
   