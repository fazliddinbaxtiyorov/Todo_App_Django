from django import forms

from .models import TodoApp


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['title', 'deadline', 'description']
        widgets = {
            'deadline': DateInput(),
        }
