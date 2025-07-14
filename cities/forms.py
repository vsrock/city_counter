from django import forms

class LetterForm(forms.Form):
    letter = forms.CharField(
        max_length=1,
        label='Enter a letter',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter a letter',
            'class': 'form-control'
        })
    )
