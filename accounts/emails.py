# from django.core.mail import send_mail
# import random
# from django.conf import settings
# from .models import User
# # import vonage
# def send_otp_via_email(email):
#     try:
#         subject = 'Djnago email sending'
#         otp = random.randint(1000, 9999)
#         message = f'Your otp is {otp}'
#         email_from = settings.EMAIL_HOST
#         send_mail(subject, message, email_from, [email])
#         user = User.objects.get(email=email)
#         user.otp_mail = otp
#         user.save()
#     except Exception as e:
#         return e


# def send_otp_sms(phone):
#     try:
#         phone_number =f'+91{phone}'
#         otp = random.randint(1000, 9999)
#         client = vonage.Client(key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET)
#         sms = vonage.Sms(client)
#         response = sms.send_message({
#         'from': settings.VONAGE_PHONE_NUMBER,
#         'to': phone_number,
#         'text': otp,
#         })
#         user = User.objects.get(phone=phone)
#         user.otp_sms = otp
#         user.save()
#     except Exception as e:
#         return e

