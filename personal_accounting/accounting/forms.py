from django import forms
from accounting.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title','amount','date','description','receipt','image']