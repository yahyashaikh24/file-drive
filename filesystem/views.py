import os
import json
from os.path import dirname
from django.shortcuts import render, redirect

from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpRequest
from .forms import FileFieldForm
from .models import FilesUpload
from . import file_process

def showfiles(request):
    if request.method == 'POST':
        form = FileFieldForm(request.POST, request.FILES)
        if form.is_valid():
            return file_process.form_valid(request,form)
    else:
        form = FileFieldForm()
        file_sys = FilesUpload.objects.filter(user_id=request.user.id)
        context = {'all_files':file_sys,'form':form}
    return render(request,'filesystem/files.html',context)

def delete_filename(request):
    loc = request.POST.get('text[file_location]')
    f_del = request.POST.get('text[file_del]')
    file_sys = FilesUpload.objects.get(user_id=request.user.id,file_path=loc,file_field=f_del)
    file_sys.delete()
    del_file(request.user.id, f_del)
    return HttpResponse(file_sys)

def del_file(user_id,f_del):
    BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
    CONTENT_DIR = os.path.join(BASE_DIR, 'content')
    MEDIA_1 = os.path.join(CONTENT_DIR ,'media')
    full_dir = os.path.join(MEDIA_1 , str(user_id),'media')
    try:
        os.remove(full_dir+'\\'+f_del)
        off_del = f_del.split('.')
        if off_del[-1] in utils.ext:
            os.remove(full_dir+'\\'+f_del+".pdf.png")
        else:
            os.remove(full_dir+'\\'+f_del+".png")
    except:
        pass

def rename_filename(request):
    loc = request.POST.get('text[file_location]')
    f_old = request.POST.get('text[file_old]')
    f_new = request.POST.get('text[file_new]')
    file_sys = FilesUpload.objects.get(user_id=request.user.id,file_path=loc,file_field=f_old)
    file_sys.file_path = '/media/'+f_new
    file_sys.file_field = f_new
    print(file_sys.file_field)
    file_sys.save()
    rename_file(request.user.id,f_old,f_new)
    return HttpResponse((request.POST.get('text[file_new]')+","+request.POST.get('text[file_location]')))

def rename_file(user_id,f_old,f_new):
    BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
    CONTENT_DIR = os.path.join(BASE_DIR, 'content')
    MEDIA_1 = os.path.join(CONTENT_DIR ,'media')
    full_dir = os.path.join(MEDIA_1 , str(user_id),'media')
    os.rename(full_dir+'\\'+f_old,full_dir+'\\'+f_new)

def search_filename(request):
    key = request.GET.get('q')
    search_query = FilesUpload.objects.filter(user_id=request.user.id,file_field__icontains=key)
    context = {'all_files':search_query}
    for i in search_query:
        print(i.thumbnail_img)
    return render(request,'filesystem/files.html',context)