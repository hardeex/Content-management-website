# Generated by Django 4.2.1 on 2023-06-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_tasks_start_date_alter_tasks_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
