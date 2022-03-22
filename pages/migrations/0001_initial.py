# Generated by Django 4.0.3 on 2022-03-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заголовок слайда')),
                ('description', models.TextField(verbose_name='Описание на слайде')),
                ('link', models.CharField(max_length=300, verbose_name='Ссылка на продук')),
                ('is_active', models.BooleanField(default=False, verbose_name='Включить/Выключить')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
