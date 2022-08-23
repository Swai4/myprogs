from django import forms
from .models import Contact

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