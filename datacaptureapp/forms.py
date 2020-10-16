from django import forms
from datacaptureapp.models import Project, Attribute, Node


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'})
        }


class CreateAttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = ['name', 'type', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter attribute name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'type': forms.Select(attrs={'class': 'form-control'}, choices=(('text', 'Text'), ('number', 'Number')))
        }


class CreateNodeForm(forms.Form):
    class Meta:
        model = Node
        fields = ['latitude', 'longitude']
        widgets = {
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'})
        }


