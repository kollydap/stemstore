from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Stock
from . models import Customer

def home(request):
	stock = Stock.objects.order_by('-list_date').filter(in_stock=True)
	return render(request, 'page/index.html', {'stock':stock})

def about(request):
	return render(request, 'page/about.html')

def contact(request):
	if request.method == "POST":
		email = request.POST["customerEmail"]
		name =  request.POST["customerName"]
		subject = request.POST["contactSubject"]
		message = request.POST["contactMessage"]
		customer = Customer(email = email, name = name, subject=subject, message=message)
		customer.save()
		print(customer)
	return render (request, 'page/contact.html')
'''
def customer(request):
	if request.method == "POST":
		email = request.POST["customerEmail"]
		name =  request.POST["customerName"]
		subject = request.POST["contactSubject"]
		message = request.POST["contactMessage"]
		customer = Customer(email = email, name = name, subject=subject, message=message)
		customer.save()
		print(customer)

	return render(request, 'page/contact.html')
	'''