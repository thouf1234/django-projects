from django import forms
from firstApp.models import movie_model
class DateInput(forms.DateInput):
    input_type = 'date'
def date_validate(value):
    year = str(value).split('-')[0]
    print(year)
    if int(year)<2012:
        raise forms.ValidationError("date must be 2012 or above")
class movie_form(forms.ModelForm):
    rdate = forms.DateField(widget=DateInput(),validators=[date_validate],label='Release Date')
    class Meta:
        model=movie_model
        fields="__all__"
