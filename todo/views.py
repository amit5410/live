from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

def todoview(request):
	all_todo_items = TodoItem.objects.all()
	return render(request, 'todo.html',
		{'all_items': all_todo_items})

def addtodo(request):
	new_item = TodoItem(content = request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('/todo/')	