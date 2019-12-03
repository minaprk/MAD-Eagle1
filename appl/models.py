from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils import timezone
import datetime


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    appointment = models.OneToOneField(
        'Appointment',
        blank=True,
        on_delete=models.CASCADE,
        null=True)
    appointment_allotted = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name


class Master(models.Model):
    master_name = models.CharField(max_length=50)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.master_name

    def rate_master(self, new_rate):
        if self.rating == 0.0:
            self.rating = new_rate
            return self.rating
        else:
            return (self.rating + new_rate) / 2


class Appointment(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    app_date = models.DateTimeField()
    vacant = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.service)

class Service(models.Model):
    service_choice = [('C', 'Coloring'), ('HC', 'Haircut'), ('HS', 'Hairstyle'), ('MU', 'Make Up'), ('M', 'Manicure'),
                      ('D', 'Depilation'), ('P', 'Pedicure'), ('S', 'Spa')]
    master = models.ManyToManyField('Master', default=None, blank=True)
    service_type = models.CharField(choices=service_choice, max_length=1, default=None, null=True)

    def __str__(self):
        return str(self.service_type)


class Editor(models.Model):
    editor_name = models.CharField(max_length=100)
    editor_surname = models.CharField(max_length=100)

    def __str__(self):
        return self.editor_name + " " + self.editor_surname


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    image = models.ImageField(blank=True, upload_to='static/img', help_text='150x150px', verbose_name='Ссылка картинки')
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.article_title

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=21))
