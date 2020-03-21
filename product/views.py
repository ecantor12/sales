#from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.
#@login_required


def product_list(request):
    if request.user.is_authenticated:
        product = Product.objects.all()
        return render(request, 'product/product_list.html', {'object_list': product})
    else:
        return HttpResponseRedirect("/accounts/login/")


def add_product(request, product_id, order_id, quantity):
	if request.user.is_authenticated:
		date = datetime.now()
		user = request.user
		order = Order.objects.get(pk=order_id)
		product = Product.objects.get(pk=product_id)
		order.product.add(product)
		order.user = user
		order.quantity = quantity
		order.sales_date = date
		order.save()
		return render(request, 'product/product_list.html', {'object_list': product})
	else:
		return HttpResponseRedirect("/accounts/login/")

def confirm_sale(request, order_id):
	if request.user.is_authenticated:
		order = Order.objects.get(pk =order_id)
		products = order.objects.all()
		total = 0
		for product in products:
			cost = product.price * order.quantity
			total = total + cost
			cost = 0
		return render(request, 'product/product_list.html', {'order': order, 'total': total })
	else:
		return HttpResponseRedirect("/accounts/login/")


def cancel_sale(request, order_id):
	if request.user.is_authenticated:
		order = Order.objects.get(pk =order_id)
		order.delete()
		return render(request, 'product/product_list.html')
	else:
		return HttpResponseRedirect("/accounts/login/")


def clean_product(request, order_id, product_id):

	if request.user.is_authenticated:

		order = Order.objects.get(pk =order_id)
		product = Product.objects.get(pk= product_id)
		order.product.remove(product)
		return render(request, 'product/product_list.html')
	else:
		return HttpResponseRedirect("/accounts/login/")
