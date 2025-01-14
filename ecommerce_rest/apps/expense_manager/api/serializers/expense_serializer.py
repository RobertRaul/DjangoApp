from rest_framework import serializers
from apps.expense_manager.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        exclude = ('created_date','modified_date','delete_date')
        