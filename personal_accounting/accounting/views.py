from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from accounting.forms import TransactionForm
from accounting.models import Transaction


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'accounting/add_transaction.html'
    success_url = reverse_lazy('transaction_list')

class TransactionListView(ListView):
    model = Transaction
    template_name = 'accounting/transaction_list.html'
    context_object_name = 'transactions'

def visit_count_view(request):
    visit_count = request.session.get('visit_count',0)
    visit_count += 1
    request.session['visit_count'] = visit_count
    return render(request,'accounting/visit_count.html',{
        'visit_count':visit_count
    })