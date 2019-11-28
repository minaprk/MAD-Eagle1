from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    #image = models.ImageField(blank=True, upload_to='static/img', help_text='150x150px', verbose_name='Ссылка картинки')

class Article(models.Model):
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    image = models.ImageField(blank=True, upload_to='static/img', help_text='150x150px', verbose_name='Ссылка картинки')
    pub_date= models.DateTimeField()

    def __str__(self):
        return self.article_title
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 21))