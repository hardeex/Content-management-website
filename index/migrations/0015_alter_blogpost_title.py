# Generated by Django 3.2.12 on 2023-05-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.TextField(max_length=255),
        ),
    ]
