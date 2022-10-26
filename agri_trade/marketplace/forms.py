from django import forms

from agri_trade.marketplace.models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name', 'category', 'variety', 'type', 'form', 'size', 'cultivation_type', 'available_volume', 'price',
            'description', 'origin', 'location', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name',
                                           }),
            'category': forms.Select(attrs={'class': 'form-control',
                                            }),
            'variety': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Variety',
                                              }),
            'type': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Type',
                                           }),
            'form': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Form',
                                           }),
            'size': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Size in mm',
                                           }),
            'cultivation_type': forms.Select(attrs={'class': 'form-control',
                                                    }),
            'available_volume': forms.NumberInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Available Volume in KG',
                                                         }),
            'price': forms.NumberInput(attrs={'class': 'form-control',
                                              'placeholder': 'Price in EUR/KG',
                                              }),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Description',
                                                 'rows': 5,
                                                 }),
            'origin': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Origin',
                                             }),
            'location': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Location',
                                               }),
            'image': forms.FileInput(attrs={'class': 'form-control',
                                            }),
        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name', 'category', 'variety', 'type', 'form', 'size', 'cultivation_type', 'available_volume', 'price',
            'description', 'origin', 'location', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           }),
            'category': forms.Select(attrs={'class': 'form-control',
                                            }),
            'variety': forms.TextInput(attrs={'class': 'form-control',
                                              }),
            'type': forms.TextInput(attrs={'class': 'form-control',
                                           }),
            'form': forms.TextInput(attrs={'class': 'form-control',
                                           }),
            'size': forms.TextInput(attrs={'class': 'form-control',
                                           }),
            'cultivation_type': forms.Select(attrs={'class': 'form-control',
                                                    }),
            'available_volume': forms.NumberInput(attrs={'class': 'form-control',
                                                         }),
            'price': forms.NumberInput(attrs={'class': 'form-control',
                                              }),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'rows': 5,
                                                 }),
            'origin': forms.TextInput(attrs={'class': 'form-control',
                                             }),
            'location': forms.TextInput(attrs={'class': 'form-control',
                                               }),
            'image': forms.FileInput(attrs={'class': 'form-control',
                                            }),
        }


class DeleteProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ()
