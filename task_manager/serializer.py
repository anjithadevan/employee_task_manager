from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True, min_length=8)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password')


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='Username', write_only=True, required=True)
    password = serializers.CharField(label='Password', write_only=True, min_length=8, required=True)

    class Meta:
        model = User
        fields = ('username', 'password')
