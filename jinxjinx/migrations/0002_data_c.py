# Generated by Django 2.1.3 on 2018-11-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jinxjinx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='c',
            field=models.CharField(default='교통', max_length=50),
        ),
    ]
