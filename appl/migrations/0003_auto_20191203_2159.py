# Generated by Django 2.2.7 on 2019-12-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0002_auto_20191203_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='name',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='vacant',
            field=models.BooleanField(default=False, null=True),
        ),
    ]