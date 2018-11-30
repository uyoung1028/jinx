# Generated by Django 2.1.3 on 2018-11-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jinxjinx', '0005_situation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentence',
            name='sen_reason',
        ),
        migrations.RemoveField(
            model_name='sentence',
            name='sen_result',
        ),
        migrations.AddField(
            model_name='sentence',
            name='cause_noun',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='sentence',
            name='cause_verb',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='sentence',
            name='effect_noun',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='sentence',
            name='effect_verb',
            field=models.CharField(default='', max_length=50),
        ),
    ]
