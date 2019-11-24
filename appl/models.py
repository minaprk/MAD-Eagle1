from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='static/img', help_text='150x150px', verbose_name='Ссылка картинки')
