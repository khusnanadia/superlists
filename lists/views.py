from django.shortcuts import redirect, render
from lists.models import Item, List
#test
def home_page(request):
	comment = ''
	if Item.objects.count() == 0:
		comment = 'yey, waktunya berlibur'
	elif Item.objects.count() < 5:
		comment = 'sibuk tapi santai'
	else:
		comment = 'oh tidak'

	return render(request, 'home.html', {'comment':comment})

	
def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))


def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))


def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	itemList = Item.objects.filter(list_id=list_id)

	comment = ''
#	if Item.objects.filter(list_id=list_id).count() == 0:
	if itemList.count() == 0:
		comment = 'yey, waktunya berlibur'
#	elif Item.objects.filter(list_id=list_id).count() < 5:
	elif itemList.count() < 5:
		comment = 'sibuk tapi santai'
#	elif Item.objects.filter(list_id=list_id).count() >= 5:
	else:
		comment = 'oh tidak'

	return render(request, 'list.html', {'list': list_, 'comment' : comment})

