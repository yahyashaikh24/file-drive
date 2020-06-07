from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class FilesUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_field = models.FileField(unique=True)
    file_path = models.FilePathField()
    thumbnail_img = models.ImageField(null=True)
    create_date = models.DateTimeField(default=datetime.datetime.now())
    modified_date = models.DateTimeField(default=datetime.datetime.now())