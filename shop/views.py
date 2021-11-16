from django.shortcuts import get_object_or_404, render
from .models import Stock

def shop(request):
	stock = Stock.objects.order_by('-list_date').filter(in_stock=True)
	return render(request,"shop/shop.html", {'stock':stock})

def stock(request, stock_id):
	stock = get_object_or_404(Stock, pk=stock_id)
	other_stock = Stock.objects.order_by('-list_date').filter(in_stock=True)

	context = {
	'stock': stock,
	'other_stock':other_stock
	}

	return render(request, 'shop/stock_details.html', context)
	