from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,VerifyOtpSerializer,VerifysmsOtpSerializer,LoginSerializer
from .models import User,Refresh_Token
# from .emails import send_otp_via_email,send_otp_sms
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterAPI(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = UserSerializer(data= data)
            if serializer.is_valid():
                serializer.save()
                # send_otp_via_email(serializer.data['email'])
                # send_otp_sms(serializer.data['phone'])
                return Response({
                    "status":200,
                    "message":"Registration successfully check mail and phone",
                    "data":serializer.data
                })
            return Response({
                "status":400,
                "message":serializer.errors
            })
        except Exception as e:
            return Response({
                "status":400,
                "message":e
            })



class VerifyOtp(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = VerifyOtpSerializer(data = data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp_mail= serializer.data['otp']
                user  = User.objects.get(email = email)
                if not user.exists():
                    return Response({
                        "status":400,
                        "message":"No user"
                    })
                if not user[0].otp_mail == otp_mail:
                    return Response({
                        "status":400,
                        "message":"wrong otp"
                    })
                user = user.first()
                user.is_verified = True
                user.save()
                return Response({
                    "status": 200,
                    "message": "otp verified",
                    "data": serializer.data
                })
        except Exception as e:
            return Response({"message":e})


class VerifyOtpSms(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = VerifysmsOtpSerializer(data = data)
            if serializer.is_valid():
                phone = serializer.data['phone']
                otp_sms= serializer.data['otp']
                user  = User.objects.filter(phone = phone)
                print(user)
                if not user.exists():
                    return Response({
                        "status":400,
                        "message":"No user"
                    })
                if not user[0].otp_sms == otp_sms:
                    return Response({
                        "status":400,
                        "message":"wrong otp"
                    })
                user = user.first()
                user.is_verified = True
                user.save()
                return Response({
                    "status": 200,
                    "message": "otp verified",
                    "data": serializer.data
                })
        except Exception as e:
            return Response({"message":e})


class LoginAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if not serializer.is_valid():
            return Response({"status":False,"message": serializer.errors})
        user = authenticate(email = serializer.data['email'],password = serializer.data['password'])
        if not user:
            return Response({"status":400,"message":"Invalid credentials"})
        refresh = RefreshToken.for_user(user)
        token=Refresh_Token.objects.create(user=user,refreshToken=str(refresh))
        token.save()
        print(token.created_at) 
        return Response({
            "status":True,
            "message":"login successful",
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })