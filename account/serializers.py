from .models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
import uuid


class UserSerializer(serializers.ModelSerializer):
    repassword = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "repassword")

    def validate(self, data):
        if data['password'] != data['repassword']:
            raise serializers.ValidationError({
                "password" : "Password fields didn't match"
            })
        
        return data

    def create(self, validated_data):
        generated_uuid = uuid.uuid4()
        user = User.objects.create_user(
            username=validated_data['username'],
        )
        password = validated_data['password']
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer): # 전체 유저 정보 조회
    #email = serializers.EmailField(read_only=True)
    #created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = User
        fields = ['userId', 'username', 'password']

class LoginSerializer(serializers.Serializer):  # 회원가입한 유저 로그인 
    username = serializers.CharField(required=True)
    #email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error":"Unable to log in with provided credentials."})
    
# class EmailVerificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'verification_code']

# class EmailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email']