from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
#	if request.method == 'POST':
#		Item.objects.create(text=request.POST['item_text'])
#		return redirect('/lists/the-only-list-in-the-world/')

	comment = ''
	if Item.objects.count() == 0:
		comment = 'yey, waktunya berlibur'
	elif Item.objects.count() < 5:
		comment = 'sibuk tapi santai'
	else:
		comment = 'oh tidak'

	items = Item.objects.all()
	return render(request, 'home.html', {'comment':comment})
#	return render(request, 'home.html')#, {'items': items, 'comment' : comment})

def view_list(request):
#	pass
	items = Item.objects.all()
	return render(request, 'list.html', {'items' : items})

def new_list(request):
#	pass
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')
