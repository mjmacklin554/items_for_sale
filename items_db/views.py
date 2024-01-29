from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item
from .forms import ItemForm


def home(request):

	list_items = Item.objects.all()

	
	return render(request, 'home.html', {'list_items': list_items})


def list_item(request):

	list_items = Item.objects.all()

	return render(request, 'list_item.html', {'list_items': list_items})


def add_item(request):
	submitted = False
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_item?submitted=True')

	else:
		form = ItemForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'add_item.html', {'form': form, 'submitted':submitted})

	
def show_list(request, list_id):
	key_item = Item.objects.get(pk=list_id) 
	return render(request, 'show_list.html', {'key_item': key_item})



	
