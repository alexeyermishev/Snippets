from django import forms
from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code', 'public']
        widgets = {
          'name': TextInput(attrs={'placeholder': 'Название сниппета'}),
          'code': Textarea(attrs={'placeholder': 'Код сниппета'}),
        }
        labels = {'name': '', 'lang': '', 'code': '', 'public': ''}

class UserForm(forms.Form):
    model = Snippet
    fields = ['name', 'lang', 'code', 'public']
    name = forms.CharField(max_length=100)
    code = forms.CharField(max_length=100)

