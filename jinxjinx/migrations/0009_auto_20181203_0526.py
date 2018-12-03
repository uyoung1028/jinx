# Generated by Django 2.1.3 on 2018-12-03 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jinxjinx', '0008_auto_20181130_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=50)),
                ('weather', models.CharField(max_length=50)),
                ('feeling', models.CharField(max_length=50)),
                ('result', models.BooleanField(max_length=50)),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinxjinx.UserSentence')),
            ],
        ),
        migrations.RemoveField(
            model_name='situation',
            name='sentence',
        ),
        migrations.DeleteModel(
            name='Situation',
        ),
    ]
