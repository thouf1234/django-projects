from django import forms
from django.core import validators
def starts_with(value):
    if str(value)[0:9]!='211518205':
        raise forms.ValidationError("college code or batch code or department code was wrong")
def gmail_verify(value):
    if str(value[len(value)-9:]).lower()!='gmail.com':
        raise forms.ValidationError("Must Be Gmail")
class studentsregister(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField(validators=[starts_with])
    email = forms.EmailField(validators=[gmail_verify])
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput,label='password(again)')
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)
    def clean_name(self):
        print("vallidating name")
        inputname = self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("The Minimum Number Of Character In The Name Field Should Be 4")
        return inputname
    def clean_rollno(self):
        print("vallidating rollno")
        inputrollno = self.cleaned_data['rollno']
        return inputrollno
    def clean_email(self):
        print("vallidating email")
        inputemail = self.cleaned_data['email']
        return inputemail
    def clean_repassword(self):
        print("password validation....")
        password=self.cleaned_data['password']
        repassword=self.cleaned_data['repassword']
        if repassword!=password:
            raise forms.ValidationError("passwords not matched")
        return repassword
    def clean_feedback(self):
        print("vallidating feedback")
        inputfeedback = self.cleaned_data['feedback']
        return inputfeedback
    def clean_bot_handler(self):
        print("vallidating bot")
        inputbot = self.cleaned_data['bot_handler']
        if len(inputbot)>0:
            raise forms.ValidationError("bot detected...form cannot be submitted!!!")
