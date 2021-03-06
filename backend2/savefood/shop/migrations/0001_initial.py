# Generated by Django 3.2 on 2021-05-04 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название:')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('description', models.TextField(blank=True, verbose_name='Описание:')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото:')),
                ('telephone', models.CharField(max_length=11, verbose_name='Телефон:')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='Адрес:')),
                ('lat', models.FloatField(blank=True, verbose_name='Широта:')),
                ('lon', models.FloatField(blank=True, verbose_name='Долгота:')),
                ('company_type', models.IntegerField(choices=[(1, 'Кафе/кофейня/бар'), (2, 'Ресторан'), (3, 'Столовая'), (4, 'Гостиница'), (5, 'Местный производитель'), (6, 'Местный фермер'), (7, 'Магазин «у дома»'), (8, 'Гипермаркет'), (9, 'Cash&Carry'), (10, 'Прилавок/киоск'), (11, 'Частное предприятие')], verbose_name='Тип компании:')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь:')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=11, verbose_name='Телефон:')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название:')),
                ('description', models.TextField(blank=True, verbose_name='Описание:')),
                ('price', models.PositiveIntegerField(verbose_name='Цена:')),
                ('quantity', models.PositiveIntegerField(verbose_name='Кол-во:')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото:')),
                ('food_type', models.IntegerField(choices=[(1, 'Мясо и мясопродукты'), (2, 'Рыба и морепродукты'), (3, 'Молоко и молокопродукты'), (4, 'Овощи и фрукты'), (5, 'Пекарня'), (6, 'Кондитерская'), (7, 'Консервы'), (8, 'Бакалея'), (9, 'Кулинария'), (10, 'Частная компания')], verbose_name='Тип продукта:')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='shop.company', verbose_name='Компания:')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('food', models.ManyToManyField(to='shop.Food')),
            ],
            options={
                'ordering': ['cart_id'],
            },
        ),
    ]
