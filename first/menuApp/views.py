from django.shortcuts import render
from .models import *
# Create your views here.


def mainView(request):
    return render(request,'menuApp/index.html', {'menus': Menu.objects.all()})

def SubView(request,path):
    splitted_path = path.split('/')
    assert len(splitted_path) > 0, ('= Draw_menu function failed =')
    print(splitted_path)
    return render(
        request, 'menuApp/index.html', {'menu_name': splitted_path[0], 'menu_item': splitted_path[-1]})

    return {'ok':'ok'}