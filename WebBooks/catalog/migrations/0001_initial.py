# Generated by Django 4.1.7 on 2023-03-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя автора', max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Введите фамилию автора', max_length=100, verbose_name='Фамилия автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Введите дату рождения', null=True, verbose_name='Дaтa рождения')),
                ('date_of_death', models.DateField(blank=True, help_text='Введите дату смерти', null=True, verbose_name='Дaтa смерти')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр книги', max_length=200, verbose_name='Жaнp книги')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите язык книги', max_length=20, verbose_name='Язык книги')),
            ],
        ),
    ]
