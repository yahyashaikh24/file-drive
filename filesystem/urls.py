from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import FileFieldView,showfiles, rename_filename,delete_filename, search_filename

app_name = 'filesystem'

urlpatterns = [
    path('files/',FileFieldView.as_view(), name='index'),
    path(r'search/', search_filename, name='search'),

    # path('',showfiles, name='index'),
    path('delete/',delete_filename, name='delete'),
    path('rename/', rename_filename, name='rename'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
