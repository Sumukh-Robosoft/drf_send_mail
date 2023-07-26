from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,VerifyOtpSerializer
from .models import User
from .emails import send_otp_via_email
class RegisterAPI(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = UserSerializer(data= data)
            if serializer.is_valid():
                serializer.save()

                x=send_otp_via_email(serializer.data['email'])
                print(x)
                return Response({
                    "status":200,
                    "message":"Registration successfully check mail",
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
                otp= serializer.data['otp']
                user  = User.objects.filter(email = email)
                if not user.exists():
                    return Response({
                        "status":400,
                        "message":"No user"
                    })
                if not user[0].otp == otp:
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
