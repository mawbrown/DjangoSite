from django import forms
from mysite_app.models import MysiteModel

# Create a form that allows you to input a title, description and image
# class MySiteForm(forms.Form):

#     title = forms.CharField(max_length=200)
#     description = forms.CharField(widget=forms.Textarea)
#     image = forms.ImageField()

# Create a Django Form from Models
class MySiteForm(forms.ModelForm):

    class Meta:
        model= MysiteModel
        fields = ['title', 'description', 'image']