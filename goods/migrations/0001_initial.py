# Generated by Django 5.0.1 on 2024-02-01 12:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='goods/images/')),
                ('preview', models.ImageField(upload_to='goods/previews/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]