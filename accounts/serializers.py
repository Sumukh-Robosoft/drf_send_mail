from rest_framework import serializers
from .models import User,UploadedFile
from cloudinary.uploader import upload

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
class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('id', 'file_url', 'created_at')
        read_only_fields = ('id', 'file_url', 'created_at')

    def create(self, validated_data):
        file = self.context['request'].data.get('file')
        upload_result = upload(file, resource_type="auto")
        return UploadedFile.objects.create(file_url=upload_result['url'])