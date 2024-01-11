from django.db import models
from django import forms
from django.core import validators
# Create your models here.

def validator_for_a(data):
    if data.lower()[0] in ['a','b']:
        raise forms.ValidationError('invalid it starts with a or b')
    #or if data.lower()[0]=='a' or 


class Student(models.Model):
    sname=models.CharField(max_length=100,primary_key=True,validators=[validator_for_a])
    sage=models.IntegerField()
    smobile=models.CharField(max_length=10,unique=True,validators=[validators.RegexValidator('[6-9]\d{9}')])
    saadhar=models.CharField(max_length=12,unique=True,validators=[validators.RegexValidator('[1-9]\d{11}')])
    span=models.CharField(max_length=10,validators=[validators.RegexValidator('[a-zA-Z][a-zA-Z0-9]{9}')])
    #in mobileno,aadhar all are digits but we need to give cf
    #because its length is more i.e 10,12
    #unique=true if it is unique then it will validate
    #pan having alphabets and digits

    def __str__(self):
        return self.sname



