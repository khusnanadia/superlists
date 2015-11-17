from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
	comment = "yey, waktunya berlibur"
	return render(request, 'home.html', {'comment': comment})

def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	return redirect('/lists/%d/' % (list_.id,))

#def add_item(request, list_id):
#	list_ = List.objects.get(id=list_id)
#	Item.objects.create(text=request.POST['item_text'], list=list_)
#	return redirect('/lists/%d/' % (list_.id,))

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	itemList = Item.objects.filter(list_id=list_id)

	comment = ''
	if itemList.count() == 0:
		comment = 'yey, waktunya berlibur'
	elif itemList.count() < 5:
		comment = 'sibuk tapi santai'
	else:
		comment = 'oh tidak'

	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'], list=list_)
		return redirect('/lists/%d/' % (list_.id,))
	return render(request, 'list.html', {'list': list_, 'comment': comment})

