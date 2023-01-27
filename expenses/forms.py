from django import forms
from .models import Expense


class ExpenseSearchForm(forms.Form):
    name = forms.CharField(required=False)
    fromdate = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    todate = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
