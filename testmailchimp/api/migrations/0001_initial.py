# Generated by Django 2.0.2 on 2018-02-04 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('fullname', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('province_state', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
    ]