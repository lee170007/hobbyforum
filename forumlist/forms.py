from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_caption', 'post_content', 'post_image',)
        # widgets = {'user_id': forms.HiddenInput()}