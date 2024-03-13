from django import forms

from .models import QForm


class QuestionFormFirst(forms.ModelForm):
    class Meta:
        model = QForm

        fields = ('email', 'company_name', 'prop_type')


class QuestionFormSecond(forms.ModelForm):
    class Meta:
        model = QForm

        fields = ('address', 'phone_number', 'is_franchise')
