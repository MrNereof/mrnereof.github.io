# Generated by Django 4.2.1 on 2023-05-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('image', models.ImageField(upload_to='paintings', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Картина',
                'verbose_name_plural': 'Картины',
            },
        ),
    ]
