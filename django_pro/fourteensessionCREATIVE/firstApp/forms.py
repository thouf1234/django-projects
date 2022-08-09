from django import forms
class djforms(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()
