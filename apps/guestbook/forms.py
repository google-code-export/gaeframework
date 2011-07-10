from gae import forms
from models import Message

class MessageAdminForm(forms.ModelForm):
    class Meta:
        model   = Message
        exclude = ['author']

class MessageInlineAdminForm(forms.ModelForm):
    class Meta:
        model   = Message
        exclude = ['author']

class MessageForm(forms.ModelForm):
    class Meta:
        model   = Message
        exclude = ['author']