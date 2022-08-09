from django import forms
from blog.models import Comment
class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.CharField()
    comments=forms.CharField(required=False,widget=forms.Textarea)#givving comments is not mandatory
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
