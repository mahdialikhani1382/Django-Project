from django.urls import path
from . import views
from accounting.views import TransactionCreateView, TransactionListView

urlpatterns = [
    path('add/',TransactionCreateView.as_view(),name='add_transaction'),
    path('',TransactionListView.as_view(),name='transaction_list'),
    path('session-view/',views.visit_count_view)
]