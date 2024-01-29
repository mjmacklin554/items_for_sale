from django.db import models


class Source(models.Model):
	name = models.CharField('Location Name', max_length=120)
	address = models.CharField(max_length=120)
	postcode = models.CharField(max_length=10)
	phone = models.CharField('Contact Phone', max_length=10)
	web = models.URLField('Website Address')
	email = models.EmailField('Email Address')

	def __str__(self):
		return self.name



class Item(models.Model):
	item_name = models.CharField('Item Name', max_length=120)
	category = models.CharField(max_length=30)
	description = models.TextField(blank=True)
	source = models.ForeignKey(Source, blank=True, null=True, on_delete=models.CASCADE)
	value = models.DecimalField(max_digits=6, decimal_places=2)
	sell =  models.DecimalField(max_digits=6, decimal_places=2)
	comments =  models.TextField(blank=True)

	def __str__(self):
		return self.item_name
