# Generated by Django 2.1.5 on 2019-02-13 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.CharField(max_length=255)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('jumlah_komen', models.CharField(max_length=255)),
                ('judul', models.CharField(max_length=255)),
                ('isi_kontent', models.TextField(max_length=255)),
            ],
        ),
    ]
