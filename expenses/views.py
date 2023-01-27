from django import forms
from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5  # how may items per page

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            fromdate = form.cleaned_data.get('fromdate', '')
            todate = form.cleaned_data.get('todate', '')
            # print(fromdate, todate)
            category = form.cleaned_data.get('category', '')
            print(category)

            filters = {}

            if name:
                filters['name__icontains'] = name
            if fromdate and todate:
                filters['date__range'] = [fromdate, todate]
            if category:
                filters['category__in'] = category

            queryset = queryset.filter(**filters)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            **kwargs
        )


class CategoryListView(ListView):
    model = Category
    paginate_by = 5
