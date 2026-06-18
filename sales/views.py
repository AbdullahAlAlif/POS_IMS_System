from django.shortcuts import render, redirect, get_object_or_404
import json
from inventory.models import Product, Category
from django.db.models.functions import Coalesce
from .forms import CustomerForm
from .models import Sale, SaleItem, Customer
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.http import HttpResponse
from django.db.models import Q


def pos_home(request):
    search_query = request.GET.get('q', '')  
    if search_query:
        # filter products by name containing the keyword and quantity > 0
        products = Product.objects.filter(
            Q(name__icontains=search_query),
            quantity__gt=0
        )
    else:
        products = Product.objects.filter(quantity__gt=0)

    return render(
        request,
        'sales/pos_home.html',
        {
            'products': products,
            'search_query': search_query  # pass back to template for keeping the search value
        }
    )



@transaction.atomic
def checkout(request):
    if request.method == 'POST':
        cust_form = CustomerForm(request.POST)
        if cust_form.is_valid():
            customer = cust_form.save()
        else:
            customer = None
        sale = Sale.objects.create(cashier=request.user, customer=customer)
        total = 0
        for key, value in request.POST.items():
            if key.startswith('product_'):
                try:
                    pid = int(key.split('_')[1])
                    qty = int(value or 0)
                except:
                    continue
                if qty <= 0:
                    continue
                product = get_object_or_404(Product, pk=pid)
                
                product.quantity = F('quantity') - qty
                product.save()
                product.refresh_from_db()
                price = product.price
                SaleItem.objects.create(sale=sale, product=product, quantity=qty, price=price)
                total += float(price) * qty
        sale.total_amount = total
        sale.save()
        return redirect('sales:receipt', sale_id=sale.id)
    return HttpResponse('Invalid method', status=405)



def receipt(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    return render(request, 'sales/receipt.html', {'sale': sale})



def sales_history(request):
    sales = Sale.objects.all().order_by('-created_at')
    return render(request, 'sales/history.html', {'sales': sales})



def sales_summary(request):
    total_amount = Sale.objects.aggregate(total=Sum('total_amount'))['total'] or 0
    total_products_sold = SaleItem.objects.aggregate(total=Sum('quantity'))['total'] or 0
    
    # Best & Worst Products based on product sold (quantity)
    products_by_sales = Product.objects.annotate(
        total_sold=Coalesce(Sum('saleitem__quantity'), 0)
    ).order_by('-total_sold')
    
    best_product = None
    worst_product = None
    has_sales = False
    
    if products_by_sales.exists():
        best_product = products_by_sales.first()
        worst_product = products_by_sales.last()
        has_sales = best_product.total_sold > 0

    # Visual bar chart data (sales by category)
    category_sales = Category.objects.annotate(
        total_sold=Coalesce(Sum('product__saleitem__quantity'), 0)
    ).order_by('-total_sold')
    
    category_names = [c.name for c in category_sales]
    category_quantities = [c.total_sold for c in category_sales]
    
    context = {
        'total_amount': total_amount,
        'total_products_sold': total_products_sold,
        'best_product': best_product,
        'worst_product': worst_product,
        'has_sales': has_sales,
        'category_names_json': json.dumps(category_names),
        'category_quantities_json': json.dumps(category_quantities),
    }
    return render(request, 'sales/summary.html', context)
