# Generated by Django 2.1.3 on 2018-11-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jinxjinx', '0002_data_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='c',
            field=models.CharField(default='', max_length=50),
        ),
    ]
