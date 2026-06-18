from django.urls import path
from . import views
app_name = 'sales'
urlpatterns = [
    path('pos/', views.pos_home, name='pos_home'),
    path('checkout/', views.checkout, name='checkout'),
    path('receipt/<int:sale_id>/', views.receipt, name='receipt'),
    path('history/', views.sales_history, name='sales_history'),
    path('summary/', views.sales_summary, name='sales_summary'),
]
