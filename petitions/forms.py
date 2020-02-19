from django import forms
from .models import Post, Comment, PostImage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body", "goal")


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("post", "author", "body")
        widgets = {
            'post': forms.HiddenInput(),
            'author': forms.HiddenInput(),
        }
