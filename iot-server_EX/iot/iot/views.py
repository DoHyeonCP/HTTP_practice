from django.shortcuts import render
from . import sub
from django.views import generic
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SecFile

# Create your views here.
def upload(request):
    if request.method == 'POST':
        file_name = request.POST['file_name']
        sec_file = request.FILES['sec_file']
        model = SecFile(file_name = file_name, sec_file = sec_file)
        model.save()
        print('upload file', file_name, sec_file = sec_file)
        msg = {'result' : 'suceess'}
    else:
        msg = {'result' : 'fail'}
    return JsonResponse(msg)

class SecFileListView(generic.ListView):
    model = SecFile
    template_name = 'iot/sec_file_list.html'
    context_object_name = 'sec_files'
