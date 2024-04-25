from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    CustomUserModel,
)

from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        # Inclua todos os campos que você deseja expor via API
        fields = (
            "id",
            "email",
            "name",
            "date_joined",
            "picture",
            "latitude",
            "longitude",
            "user_type",
            "password",
            "gender",
            "preferred_contact",
            "phone",
            "address",
            "post_code",
            "birth_date",
        )
        
        extra_kwargs = {
            "password": {"write_only": True},
            # Garantir que campos sensíveis não sejam manipuláveis
            "is_staff": {"read_only": True},
            "is_superuser": {"read_only": True},
            "user_permissions": {"read_only": True},
            "groups": {"read_only": True},
            "date_joined": {"read_only": True},
        }
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get('password', instance.password))
        return super(UserSerializer, self).update(instance, validated_data)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = {
            'latitude': self.user.latitude,
            'longitude': self.user.longitude,
        }
        return data