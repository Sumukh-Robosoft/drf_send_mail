from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['email','password','is_verified','phone']



class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_mail = serializers.CharField()

class VerifysmsOtpSerializer(serializers.Serializer):
    phone = serializers.CharField()
    otp_sms = serializers.CharField()