from django.core.mail import send_mail
from django.conf import settings
from .models import User
from .utils import generate_otp

def send_otp_via_email(email):
    subject = "Your account verification email"
    otp = generate_otp()
    message = f"Your OTP is {otp}. It will expire in 5 minutes."

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

    user = User.objects.get(email=email)
    user.otp = otp
    user.otp_attempts = 0
    user.save(update_fields=["otp", "otp_attempts"])

    return otp
