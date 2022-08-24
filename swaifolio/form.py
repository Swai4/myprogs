from django import forms
from django_svg_image_form_field import SvgAndImageFormField
from .models import Profile , Contact, Portfolio, Services, Skill

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []
        field_classes = {
            'avatar': SvgAndImageFormField,
        }

class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs): 
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['size'] = 50
        self.fields['email'].widget.attrs['size'] = 50

    class Meta:
        model = Contact
        fields = ['name', 'email','message']
    
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                #'placeholder': 'Write your name here'
            }
        )
    )

    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'style': 'border-color: green;'})
    )

    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
        #help_text='Write here your message!'
    )


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }
    