from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.IntegerField(default=0)

class Order(models.Model):
	sales_date = models.DateTimeField('sales date')
	quantity = models.IntegerField(default=0)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

