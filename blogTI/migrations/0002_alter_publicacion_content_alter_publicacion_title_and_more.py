# Generated by Django 4.2.4 on 2023-08-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogTI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='title',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
