#here we are creating django forms and sending to html page via urls

from django import forms
from app.models import *
from app.views import *

#from django module we are importing forms




class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        #from models student table we are assigning
        fields='__all__'
        #all the fields in a student table data we are getting
    botcatcher=forms.CharField(max_length=10,required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('invalid')    
