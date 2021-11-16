from django.db import models
from datetime import datetime
from store.utils import unique_slug_generator
from django.db.models.signals import pre_save


class Stock(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=250, null=True, blank=True)
	name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.IntegerField()
	photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
	in_stock = models.BooleanField(default=True)
	list_date = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.title

	

def slug_generator(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Stock)

