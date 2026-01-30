import random
from datetime import timedelta
from rest_framework_simplejwt.tokens import AccessToken



OTP_TOKEN_LIFETIME_MINUTES = 5
MAX_OTP_ATTEMPTS=5
# RESEND_SECONDS=30

def generate_otp():
    return f"{random.randint(100000,999999)}"# 6 digits otp


def make_otp_token(email: str) -> str:
    # a short time JWT used for otp verification
    token = AccessToken()
    token.set_exp(lifetime=timedelta(minutes=OTP_TOKEN_LIFETIME_MINUTES))

    # claims 
    token["purpose"] = "otp_verify"
    token["email"] = email

    return str(token)


# def can_resend(user):
#     # if otp is not created 
#     # user can resend after 30 seconds only
#     # eg 12:00:00 so after 12:00:30 
#     if not user.otp_created_at:
#         return True
#     return timezone.now() > user.otp_created_at + timedelta(seconds=RESEND_SECONDS)