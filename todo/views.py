from django.shortcuts import render,HttpResponseRedirect
from .models import ToDo
from . import models
# Create your views here.
def home(request):
    return render(request,'base.html')

def ViewToDo(request):
    if request.POST.get('add'):
        save = request.POST.get('add')
        models.ToDo.objects.create(to_do_text=save)
        final = ToDo.objects.all()
        return render(request,'todo/view.html',{
            'all_items':final
        })
    else :
        save = request.POST.get('add')
        final = ToDo.objects.all()    
        return render(request,'todo/view.html',{
            'all_items':final
        })
def deleteToDo(request,todos_id):
    a=ToDo.objects.get(id=todos_id)
    a.delete()
    return HttpResponseRedirect('/')


