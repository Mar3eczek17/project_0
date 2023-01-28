from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 12  # how may items per page

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            fromdate = form.cleaned_data.get('fromdate', '')
            todate = form.cleaned_data.get('todate', '')
            category = form.cleaned_data.get('category', '')
            order_by = form.cleaned_data.get('order_by', '')
            sort_descending = form.cleaned_data.get('sort_descending', '')

            filters = {}

            if name:
                filters['name__icontains'] = name
            if fromdate and todate:
                filters['date__range'] = [fromdate, todate]
            if category:
                filters['category__in'] = category

            queryset = queryset.filter(**filters)

            if order_by:
                if sort_descending:
                    queryset = queryset.order_by(order_by).reverse()
                else:
                    queryset = queryset.order_by(order_by)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            **kwargs
        )


class CategoryListView(ListView):
    model = Category
    paginate_by = 5
