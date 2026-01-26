from django import forms
from accounts.models import AdminUser

class CreateSubAdminForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)

    # for parent selection only seen by super admins
    parent_id = forms.ModelChoiceField(
        queryset=AdminUser.objects.filter(is_super_admin=False),
        required=False,
        empty_label="-- Select Parent (Super Admin only) --"
    )


    def clean_email(self):
        email=self.cleaned_data["email"].lower()
        if AdminUser.objects.filter(email=email).exists():
            raise forms.ValidationError("email already exists")

        return email            