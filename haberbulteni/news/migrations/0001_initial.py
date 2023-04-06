# Generated by Django 4.1.6 on 2023-02-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Makale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar', models.CharField(max_length=150)),
                ('baslik', models.CharField(max_length=120)),
                ('aciklama', models.CharField(max_length=200)),
                ('metin', models.TextField()),
                ('sehir', models.CharField(max_length=120)),
                ('yayinlanma_tarihi', models.DateField()),
                ('aktif', models.BooleanField(default=True)),
                ('yaratilma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
