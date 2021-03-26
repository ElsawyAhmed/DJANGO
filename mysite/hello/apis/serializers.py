from rest_framework import serializers
from .. models import Movie
from django.contrib.auth.models import User
# from django.db import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Movie
        fields = '__all__'


class UserRegister(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['username','email', 'password']

    def save(self, **kwargs):
        user = User(
            email = self.validated_data.get('email'),
            username = self.validated_data.get('username'),
            password = self.validated_data.get('password')
        )
        if user:
            user.save()
        else:
            raise serializers.ValidationError({
                    'error': 'Something wrong happened!'
            })