from django import forms
class session_forms_name(forms.Form):
    name = forms.CharField()
class session_forms_age(forms.Form):
    age=forms.IntegerField()
class session_forms_gf(forms.Form):
    gf=forms.CharField()
