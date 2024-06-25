from rest_framework.routers import DefaultRouter
from apps.expense_manager.api.views.expenses_viewsets import *

router = DefaultRouter()

router.register(r'expense',ExpenseViewSet,basename='expense')

urlpatterns = router.urls