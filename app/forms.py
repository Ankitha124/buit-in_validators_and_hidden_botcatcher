from django import forms
from django.core import validators


def validate_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('data is not valid')

def validate_length(name):
    if len(name)<=5:
        raise forms.ValidationError('data is less than 5')




class StudentForms(forms.Form):
    sname=forms.CharField(max_length=100, validators=[validate_a,validators.MinLengthValidator(4)])
    sage=forms.IntegerField()
    email=forms.EmailField()
    Remail=forms.EmailField()
    url=forms.URLField()
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

     
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['Remail']
        if e!=re:
            raise forms.ValidationError('email is not matching')
        
        
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']


        if len(bot)>0:
            raise forms.ValidationError('bot is entering the data ')