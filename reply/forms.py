from django import forms
from .models import Reply

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_content', 'reply_image',)
        # widgets = {'user_id': forms.HiddenInput()}