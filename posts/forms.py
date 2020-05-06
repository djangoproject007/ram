from django import forms
from .models import Post


class MakePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
        ]