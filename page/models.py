from django.db import models
from datetime import datetime

class Customer(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	subject = models.CharField(max_length=200)
	message = models.TextField()
	date = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.name

class Suscribe(models.Model):
	email = models.EmailField(max_length=200)
	def __str__(self):
		return self.email
