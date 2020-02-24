from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoView(response):
    all_todo_items = TodoItem.objects.all()
    return render(response, "todo.html", {'all_items' : all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
    # create a new todo all_items
    # save
    # redirect the browser to '/todo/'

def deleteTodo(response, todo_id):
    item_tobeDeleted = TodoItem.objects.get(id = todo_id)
    item_tobeDeleted.delete()
    return HttpResponseRedirect('/todo/')