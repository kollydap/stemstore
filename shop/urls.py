from django.urls import path
from . import views


 
urlpatterns = [
	path('',views.shop, name='shop'),
	path('<int:stock_id>',views.stock, name='stock'),
]