# Generated by Django 4.2.1 on 2023-06-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20230529_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(default='Uncategorized', max_length=150),
        ),
    ]