from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from agri_trade.accounts.models import Company

UserModel = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 }))

    class Meta:
        model = UserModel


class CustomRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True,
                                 max_length=30,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(required=True,
                                max_length=30,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email Address',
                                                           'class': 'form-control',
                                                           }))
    username = forms.CharField(required=True,
                               max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if UserModel.objects.filter(email=email):
            raise ValidationError('Email already exists!')

        if UserModel.objects.filter(username=username):
            raise ValidationError('Username already exists!')

        return self.cleaned_data


class EditAccountForm(forms.ModelForm):
    first_name = forms.CharField(required=True,
                                 max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               }))
    last_name = forms.CharField(required=True,
                                max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           }))
    username = forms.CharField(required=True,
                               max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             }))

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email')


class EditCompanyForm(forms.ModelForm):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         }))
    vat = forms.CharField(max_length=25,
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                        }))
    address = forms.CharField(max_length=200,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            }))
    postcode = forms.CharField(max_length=15,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             }))
    location = forms.CharField(max_length=25,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             }))
    country = forms.CharField(max_length=15,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            }))
    description = forms.CharField(max_length=500,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'rows': 5,
                                                               }))

    class Meta:
        model = Company
        fields = ('name', 'vat', 'address', 'postcode', 'location', 'country', 'description')

