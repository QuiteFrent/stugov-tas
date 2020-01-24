from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("post", "author", "body")
        widgets = {
            'post': forms.HiddenInput(),
            'author': forms.HiddenInput(),
        }
