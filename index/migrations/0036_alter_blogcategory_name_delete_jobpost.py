# Generated by Django 4.2.1 on 2023-06-24 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0035_alter_comment_level_alter_comment_lft_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.DeleteModel(
            name='JobPost',
        ),
    ]