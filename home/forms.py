from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets

from django import forms
from home.models import Contact_us

class ContactUsform(ModelForm):
    class Meta:
        model=Contact_us
        fields='__all__'

        widgets={
            'email' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
            'address' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your address'}),
            'zipCode' :forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Zip Code'}),
            'queries' :forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Queries Here !'})
        }





