from django import forms
from .models import UserProfileData


class EditInfo(forms.ModelForm):
    class Meta:
        model = UserProfileData
        fields = [
            "status",
            "avatar",
            "linkedin",
            "secondary_email",
            "phone_number",
            "fb",
            "instagram",
            "github",
        ]
