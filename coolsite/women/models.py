from django.db import models


# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255) # текстовое поле ("символы"), макс длина
    content = models.TextField(blank=True) # текстовое поле, blank=True - м.б. пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/") # ссылка на фото, upload_to - каталог куда загружать
    # %Y/%m/%d/ - год, месяц, день (шаблон)
    time_create = models.DateTimeField(auto_now_add=True) #auto_now_add = True - поле принимает значение
    # времени при добавлении записи, и больше меняться не будет
    time_update = models.DateTimeField(auto_now=True) #auto_now = True - поле меняется каждый раз при изменении записи
    is_published = models.BooleanField(default=True)
