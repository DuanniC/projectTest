# Generated by Django 3.1rc1 on 2020-07-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=9)),
                ('address', models.CharField(max_length=70)),
                ('address_number', models.CharField(max_length=10)),
                ('neighborhood', models.CharField(max_length=50)),
                ('complement', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ean', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=70)),
                ('fullname', models.CharField(max_length=70)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='picture')),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
