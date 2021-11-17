from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Stock

def shop(request):
	stock = Stock.objects.order_by('-list_date').filter(in_stock=True)
	paginator = Paginator(stock, 9)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)

	context = {
		'stock': paged_listings,
	}
	return render(request,"shop/shop.html", context)

def stock(request, stock_id):
	stock = get_object_or_404(Stock, pk=stock_id)
	other_stock = Stock.objects.order_by('-list_date').filter(in_stock=True)

	context = {
	'stock': stock,
	'other_stock':other_stock
	}

	return render(request, 'shop/stock_details.html', context)
	