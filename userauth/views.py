from rest_framework import generics
from rest_framework.permissions import IsAdminUser 
from .models import User , ToDo

# List all users
class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    # serializer class
    permission_classes = [IsAdminUser]
