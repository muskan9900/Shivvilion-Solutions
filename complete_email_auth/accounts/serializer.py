from rest_framework import serializers
from .models import User

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "is_verified"]
        read_only_fields = ["is_verified"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)   # password hashing 
        user.save()
        return user


class verifyAccountSerializer(serializers.Serializer):
    email= serializers.EmailField()
    otp = serializers.CharField()
    otp_token = serializers.CharField()

class ResendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()

       
    