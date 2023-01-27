from django import forms
from .models import Expense, Category


class ExpenseSearchForm(forms.Form):
    name = forms.CharField(required=False)
    fromdate = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    todate = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
