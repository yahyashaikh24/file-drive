import os
import json
from os.path import dirname
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpRequest
from .forms import FileFieldForm
from .models import FilesUpload
from accounts.models import Activation
from . import utils
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image 
from django.conf import settings
import filetype
from extract_icon import *
import urllib.parse as urllib


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'filesystem/upload.html'  # Replace with your template.
    success_url =  'index' # Replace with your URL or reverse().
    FileField = FilesUpload()
    fs = FileSystemStorage()

    def check_media_dir(self):
        BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
        CONTENT_DIR = os.path.join(BASE_DIR, 'content')
        MEDIA_1 = os.path.join(CONTENT_DIR ,'media')
        full_dir = os.path.join(MEDIA_1 , str(self.request.user.id),'media')
        if os.path.exists(full_dir):
            settings.MEDIA_ROOT = full_dir
        else:
            user = str(self.request.user.id)
            media = 'media'
            path = os.path.join(MEDIA_1,user)
            os.mkdir(path)
            path = os.path.join(path,media)
            make_media= os.mkdir(path)
            settings.MEDIA_ROOT = make_media
        return settings.MEDIA_ROOT

    def auth_files(self,file_path):
        uni_file = FilesUpload.objects.filter(user_id=self.request.user.id,file_path=file_path)
        if len(uni_file) == 0:
            return True
        else:
            return False

    def pdf_con(self,media_dir,filename):
        img = convert_from_bytes(open(os.path.join(media_dir,str(filename)), 'rb').read())
        thumb_img = os.path.join(media_dir,(str(filename)+'.png')) 
        img[0].save(thumb_img)
        thumb_path = os.path.join('media\\',str(self.request.user.id)+'\\','media\\',str(filename)+'.png')
        return thumb_path

    def exe_con(self,media_dir,filename):
        filepath = os.path.join(media_dir,str(filename))
        extractor = ExtractIcon(filepath)
        groups = extractor.get_group_icons()
        im1 = extractor.export(groups[0])
        thumb_img = os.path.join(media_dir,(str(filename)+'.png'))
        im1.save(thumb_img)
        thumb_path = os.path.join('media\\',str(self.request.user.id)+'\\','media\\',str(filename)+'.png')
        return thumb_path

    def form_valid(self,form):
        request = self.request
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        for f in files:
            filename = f.name
            f_url = self.fs.url(filename)
            auth = self.auth_files(f_url)
            f_url = urllib.unquote_plus(f_url)
            # f = urllib.unquote_plus(f.name)
            if auth == True:
                media_dir = self.check_media_dir()
                file_up = FilesUpload.objects.create(user_id=request.user.id, file_path=f_url, file_field=f)
                f_dir = os.path.join(media_dir,file_up.file_field.name)
                print(media_dir)
                os.rename(f_dir,media_dir+'\\'+f.name)
                chk_type = os.path.join(media_dir,(str(filename)))
                kind = filetype.guess(chk_type)
                # try:
                #     mime_type = kind.mime.split('/')
                #     print("filetype",mime_type)
                # except:
                django_mime_type = f.content_type.split('/')
                print(django_mime_type)
                mime_type = kind.mime.split('/')
                print(mime_type[1])
                if mime_type[0] == 'application':
                    thumb_path = os.path.join('media\\',str(self.request.user.id)+'\\','media\\','cog.svg')
                    if django_mime_type[1] in utils.mimes:
                        utils.off_pdf_thum(django_mime_type[1],chk_type,(chk_type+'.pdf'))
                        thumb_path = utils.pdf_con(media_dir=media_dir,filename=filename,user_id=request.user.id)
                        os.remove(os.path.join(media_dir,str(filename+".pdf")))
                    elif mime_type[1] == 'pdf':
                        thumb_path = self.pdf_con(media_dir=media_dir,filename=filename)
                    elif mime_type[1] == 'x-msdownload':
                        thumb_path = self.exe_con(media_dir,filename)
                    elif mime_type[1] == 'font-sfnt':
                        thumb_path = utils.font_ext(media_dir,filename,user_id=request.user.id)
                    elif mime_type[1] == 'x-lzip' or 'zip' or 'x-tar' or 'x-rar-compressed' or 'gzip' or 'x-7z-compressed' or 'x-unix-archive' or 'x-compress':
                        thumb_path = os.path.join('media\\',str(self.request.user.id)+'\\','media\\','arch.svg')
                    else:
                        pass 
                elif mime_type[0] == 'image':
                    img = Image.open(chk_type)
                    img.thumbnail((1000, 1000))
                    thumb_img = os.path.join(media_dir,(str(filename)+'.png')) 
                    img.save(thumb_img)
                    thumb_path = os.path.join('media\\',str(self.request.user.id)+'\\','media\\',str(filename)+'.png')
                thumb_update = FilesUpload.objects.filter(id=file_up.id)
                thumb_path = thumb_path.replace('\\','\\\\')
                
                thumb_update.update(thumbnail_img=thumb_path,file_field=f.name) 
            else:
                pass
        return redirect('index')
        
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def showfiles(request):
    file_sys = FilesUpload.objects.filter(user_id=request.user.id)
    context = {'all_files':file_sys}
    # for i in file_sys:
    #     print(i.file_field)
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