from django import forms
from firstApp.models import employee_crud_fdv_model
class employee_form(forms.ModelForm):
    class Meta:
        model=employee_crud_fdv_model
        fields='__all__'
