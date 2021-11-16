from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Stock

def home(request):
	stock = Stock.objects.order_by('-list_date').filter(in_stock=True)
	return render(request, 'page/index.html', {'stock':stock})

def about(request):
	return render(request, 'page/about.html')