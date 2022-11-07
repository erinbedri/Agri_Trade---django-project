from django import forms

from agri_trade.user_messages.models import Message


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'body')
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Your Subject',
                                              }),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Your Message',
                                          'rows': 5,
                                          }),
        }


class DeleteMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ()


class ReplyMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('body', )
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Your Message',
                                          'rows': 5,
                                          }),
        }