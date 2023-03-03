from rest_framework import serializers
from .models import ToDo , User
from django.contrib.auth.hashers import make_password

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ToDoRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo 
        fields = '__all__'

class RegisterNewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password' , 'name')
        extra_kwargs ={'password' :{'write_only' : True}}
        
        def create(self , validated_data):
            password = validated_data.pop('password' , None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance
