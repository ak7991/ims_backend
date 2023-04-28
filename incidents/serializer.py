from rest_framework import serializers
from .models import *  # Importing all models
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']

        # This allows any API call to the /api/users to only show username 
        # and not the password
        extra_kwargs = {'password': {  
            'write_only': True,
            'required': True,
        }}

    def create(self, validated_data):  # Create user with hashed password
        user = User.objects.create_user(**validated_data)
        # New token for every new user
        Token.objects.create(user=user)

        return user
