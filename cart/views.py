from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Stock
from django.http import JsonResponse

def cart_summary(request):
	return render(request, 'cart/cart.html') 

def cart_add(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		stock_id = int(request.POST.get('stockid'))
		product = get_object_or_404(Stock, id=stock_id)
		cart.add(stock=stock)
		response = JsonResponse({'test':'data'})
		return response