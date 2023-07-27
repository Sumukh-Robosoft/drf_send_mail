from rest_framework import serializers
from .models import User,Refresh_Token

class UserSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password = serializers.CharField()
    phone=serializers.CharField()
    
    def create(self, validated_data):
        user = User.objects.create(email= validated_data['email'],phone=validated_data['phone'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data



class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_mail = serializers.CharField()

class VerifysmsOtpSerializer(serializers.Serializer):
    phone = serializers.CharField()
    otp_sms = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

# class RefreshSerializer(serializers.Serializer):
#     user = serializers.CharField()
#     refreshToken = serializers.CharField()

#     def createToken(self,validate_data):
#         token=RefreshToken.create(user=validate_data['user'],refreshToken=validate_data['refresh'])
#         token.save()
#         return validate_data

