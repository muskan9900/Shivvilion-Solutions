import random
from datetime import timedelta
from django.utils import timezone

OTP_EXPIRY_MINUTES=10
MAX_OTP_ATTEMPTS=5
RESEND_SECONDS=30

def generate_otp():
    return f"{random.randint(100000,999999)}"# 6 digits otp

def is_otp_expired(user):
    if not user.otp_created_at:
        return True
    return timezone.now() > user.otp_created_at + timedelta(minutes=OTP_EXPIRY_MINUTES)

def can_resend(user):
    if not user.otp_created_at:
        return True
    return timezone.now() > user.otp_created_at + timedelta(seconds=RESEND_SECONDS)