from django.contrib.auth.forms import UserCreationForm
"""
    A form that creates a user, from the given username and password.
    It Matches Password1 and Password2.
    It provides a save method to save user in DB.
"""
from django.contrib.auth.models import User
# Read about User Pre-defined model at - https://docs.djangoproject.com/en/1.11/ref/contrib/auth/


class UserRegistrationForm(UserCreationForm):
    class Meta:
        # Provide an association between the ModelForm and a model
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        model = User
        # Read about User Pre-defined model at - https://docs.djangoproject.com/en/1.11/ref/contrib/auth/
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2"
        ]