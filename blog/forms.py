from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    """To create a form for collecting comments."""
    class Meta:
        model = Comment
        exclude = ["post","initials","color"]
        labels = {
            "name": "Your name",
            "email": "Your email",
            "text": "Your comment"
        }



