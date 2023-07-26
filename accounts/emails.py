from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User

def send_otp_via_email(email):
    try:
        subject = 'Djnago email sending'
        otp = random.randint(1000, 9999)
        message = f'Your otp is {otp}'
        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [email])
        user = User.objects.get(email=email)
        user.otp = otp
        user.save()
    except Exception as e:
        return e


