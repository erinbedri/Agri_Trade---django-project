from django import forms

from agri_trade.user_messages.models import Message


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Your Message',
                                          'rows': 5,
                                          }),
        }


class DeleteMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ()
