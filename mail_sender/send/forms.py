from tkinter import Widget
from django import forms
from .models import Info

class SendEmailForm(forms.ModelForm):
    message = forms.Textarea()
    
    class Meta:
        model = Info
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['subject'].widget.attrs.update({'class':'subject', 'placeholder': 'Subject'})
           self.fields['receiver_name'].widget.attrs.update({'class':'receiver_name', 'placeholder': 'Receiver Name'})
           self.fields['receiver_email'].widget.attrs.update({'class':'receiver_email', 'placeholder': 'Receiver email'})
           self.fields['message'].widget.attrs.update({'class': 'message', 'placeholder': 'Message'})
           
