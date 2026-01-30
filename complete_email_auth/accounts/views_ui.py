from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError

from .forms import RegisterForm, VerifyOTPForm, ResendOTPForm
from .serializer import UserSerializer
from .emails import send_otp_via_email
from .models import User
from .utils import make_otp_token, MAX_OTP_ATTEMPTS


def register_page(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        serializer = UserSerializer(data=form.data)
        if serializer.is_valid():
            user = serializer.save(is_verified=False)

            send_otp_via_email(user.email)

            # create OTP-session JWT and store in session
            request.session["otp_token"] = make_otp_token(user.email)
            request.session["otp_email"] = user.email

            messages.success(request, "OTP sent to your email.")
            return redirect(reverse("verify_page") + f"?email={user.email}")

        messages.error(request, serializer.errors)

    return render(request, "auth/register.html", {"form": form})


def verify_page(request):
    initial_email = request.GET.get("email", "")
    form = VerifyOTPForm(request.POST or None, initial={"email": initial_email})

    if request.method == "POST":
        if not form.is_valid():
            messages.error(request, "Invalid data.")
            return render(request, "auth/verify.html", {"form": form})

        email = form.cleaned_data["email"].strip().lower()
        otp = str(form.cleaned_data["otp"]).strip()

        otp_token = request.session.get("otp_token")
        if not otp_token:
            messages.error(request, "OTP session missing/expired. Please resend OTP.")
            return redirect(reverse("resend_page"))

        # Validate JWT expiry + purpose + email match
        try:
            token = AccessToken(otp_token)
        except TokenError:
            messages.error(request, "OTP expired. Please resend OTP.")
            return redirect(reverse("resend_page") + f"?email={email}")

        if token.get("purpose") != "otp_verify":
            messages.error(request, "Invalid OTP session token.")
            return redirect(reverse("resend_page") + f"?email={email}")

        if token.get("email") != email:
            messages.error(request, "Email mismatch. Please resend OTP.")
            return redirect(reverse("resend_page") + f"?email={email}")

        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(request, "User not found.")
            return render(request, "auth/verify.html", {"form": form})

        if user.is_verified:
            messages.info(request, "Already verified.")
            return redirect("verified_page")

        if user.otp_attempts >= MAX_OTP_ATTEMPTS:
            messages.error(request, "Too many attempts. Please resend OTP.")
            return redirect(reverse("resend_page") + f"?email={email}")

        if str(user.otp).strip() != otp:
            user.otp_attempts += 1
            user.save(update_fields=["otp_attempts"])
            messages.error(request, f"Wrong OTP. Attempts: {user.otp_attempts}")
            return render(request, "auth/verify.html", {"form": form})

        # success
        user.otp = None
        user.otp_attempts = 0
        user.is_verified = True
        user.save(update_fields=["is_verified", "otp", "otp_attempts"])

        # clear otp session
        request.session.pop("otp_token", None)
        request.session.pop("otp_email", None)

        messages.success(request, "Account verified successfully ")
        return redirect("verified_page")

    # GET prefill
    # gets the email automatically in the form 
    if request.method == "GET" and initial_email:
        form = VerifyOTPForm(initial={"email": initial_email})

    return render(request, "auth/verify.html", {"form": form})


def resend_page(request):
    form = ResendOTPForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"].strip().lower()
            user = User.objects.filter(email=email).first()

            if not user:
                messages.error(request, "User not found.")
            elif user.is_verified:
                messages.info(request, "Already verified.")
                return redirect("verified_page")
            else:
                send_otp_via_email(email)

                # generate a NEW otp_token  (fresh 5 minutes)
                request.session["otp_token"] = make_otp_token(email)
                request.session["otp_email"] = email

                messages.success(request, "OTP resent. Check your email.")
                return redirect(reverse("verify_page") + f"?email={email}")

    return render(request, "auth/resend.html", {"form": form})


def verified_page(request):
    return render(request, "auth/verified.html")
