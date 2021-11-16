class Cart(object):
	"""docstring for """
	
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get('skey')
		if 'skey' not in request.session:
			cart = self.session['skey']={}
		self.cart = cart

	def add(self, stock):
		"""
		Adding and updating the users basket session data

		"""
		stock_id = stock.id

		if stock_id not in self.cart:
			self.cart[stock_id] = {'price':stock.price}

		self.modified = True