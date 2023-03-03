from rest_framework import generics , status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser , AllowAny , IsAuthenticated
from .models import User , ToDo
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from .serializers import UserListSerializer , ToDoRetriveSerializer , RegisterNewUserSerializer


# List all users
class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]

# show all to do's of a particular user
class ShowToDo(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoRetriveSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class RegisterNewUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = RegisterNewUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getUserDetail(APIView):
    # authentication_classes = [authentication.TokenAuthentication]

    def post(self , request , format = 'json'):
        var = request.META.get('HTTP_AUTHORIZATION') # this prints the jwt token
        print(var)
        data = {
            "username":request.user.username,
            "email":request.user.email,
            "name":request.user.name
        }
        # username = request.user.username
        # email = request.user.email
        # name = request.user.name
        return Response(data)

class getUserToDo(APIView):

    def post(self , request , format = 'json'):
        print(request.user)
        dataset = ToDo.objects.filter(user = request.user)
        print(dataset)
        data = ToDoRetriveSerializer(dataset , many = True).data
        return Response(data)


# register new user using token and stuff
# class RegisterNewUser(APIView):
#     permission_classes = [AllowAny]

#     def post(self , request):
#         reg_serializer = RegisterNewUserSerializer(data = request.data)
#         if reg_serializer.is_valid():
#             newUser = reg_serializer.save()
#             if newUser :
#                 return Response(status =status.HTTP_201_CREATED )
#         return Response(reg_serializer.errors , status = status.HTTP_400_BAD_REQUEST)