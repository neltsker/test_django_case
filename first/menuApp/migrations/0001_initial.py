# Generated by Django 5.0.1 on 2024-02-08 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name of menu')),
                ('description', models.TextField(blank=True, max_length=300, verbose_name='desc of menu')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name of Item')),
                ('description', models.TextField(blank=True, max_length=300, verbose_name='desc of item')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MenuItems', to='menuApp.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menuApp.menuitem')),
            ],
            options={
                'verbose_name': 'пункт меню',
                'verbose_name_plural': 'пункт меню',
                'ordering': ['id'],
            },
        ),
    ]
