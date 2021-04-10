from django import forms
from .models import *
  
class PostForm(forms.ModelForm):
  
    class Meta:
        model = Post
        fields = ['Title', 'Description', 'Image', 'Amount']

        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
            'Image': forms.FileInput(attrs={'class':'form-control'}),
            'Amount': forms.NumberInput(attrs={'class':'form-control'})
        }