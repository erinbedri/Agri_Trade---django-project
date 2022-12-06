from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from agri_trade.accounts.models import Company

UserModel = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    USERNAME_PLACEHOLDER = 'Username'
    PASSWORD_PLACEHOLDER = 'Password'

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': USERNAME_PLACEHOLDER,
                'class': 'form-control',
            }))

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': PASSWORD_PLACEHOLDER,
                'class': 'form-control',
                'id': 'password',
            }))

    remember_me = forms.BooleanField(
        required=False
    )

    class Meta:
        model = UserModel


class CustomRegistrationForm(UserCreationForm):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_PLACEHOLDER = 'First Name'

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_PLACEHOLDER = 'Last Name'

    EMAIL_PLACEHOLDER = 'Email Address'

    USERNAME_MAX_LENGTH = 30
    USERNAME_PLACEHOLDER = 'Username'

    PASSWORD1_PLACEHOLDER = 'Password'

    PASSWORD2_PLACEHOLDER = 'Confirm Password'

    EMAIL_VALIDATION_ERROR_MESSAGE = 'Email already exists!'
    USERNAME_VALIDATION_ERROR_MESSAGE = 'Username already exists!'

    first_name = forms.CharField(
        required=True,
        max_length=FIRST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': FIRST_NAME_PLACEHOLDER,
                   'class': 'form-control',
                   }))

    last_name = forms.CharField(
        required=True,
        max_length=LAST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': LAST_NAME_PLACEHOLDER,
                   'class': 'form-control',
                   }))

    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': EMAIL_PLACEHOLDER,
                   'class': 'form-control',
                   }))

    username = forms.CharField(
        required=True,
        max_length=USERNAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': USERNAME_PLACEHOLDER,
                   'class': 'form-control',
                   }))

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': PASSWORD1_PLACEHOLDER,
                   'class': 'form-control',
                   'data-toggle': 'password',
                   'id': 'password',
                   }))

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': PASSWORD2_PLACEHOLDER,
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
            raise ValidationError(self.EMAIL_VALIDATION_ERROR_MESSAGE)

        if UserModel.objects.filter(username=username):
            raise ValidationError(self.USERNAME_VALIDATION_ERROR_MESSAGE)

        return self.cleaned_data


class EditAccountForm(forms.ModelForm):
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MAX_LENGTH = 30

    USERNAME_MAX_LENGTH = 30

    first_name = forms.CharField(
        required=True,
        max_length=FIRST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   }))

    last_name = forms.CharField(
        required=True,
        max_length=LAST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   }))

    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   }))

    username = forms.CharField(
        required=True,
        max_length=USERNAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   }))

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email')


class EditCompanyForm(forms.ModelForm):
    NAME_MAX_LENGTH = 100

    VAT_MAX_LENGTH = 25

    ADDRESS_MAX_LENGTH = 200

    POSTCODE_MAX_LENGTH = 15

    LOCATION_MAX_LENGTH = 25

    DESCRIPTION_MAX_LENGTH = 500

    DESCRIPTION_ROWS = 5

    name = forms.CharField(
        max_length=NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   }))

    vat = forms.CharField(
        max_length=VAT_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   }))

    address = forms.CharField(
        max_length=ADDRESS_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   }))

    postcode = forms.CharField(
        max_length=POSTCODE_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   }))

    location = forms.CharField(
        max_length=LOCATION_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   }))

    country = CountryField().formfield(
        widget=CountrySelectWidget(
           attrs={"class": "form-control"}
        )
    )

    description = forms.CharField(
        max_length=DESCRIPTION_MAX_LENGTH,
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': DESCRIPTION_ROWS,
                   }))

    class Meta:
        model = Company
        fields = ('name', 'vat', 'address', 'postcode', 'location', 'country', 'description')

