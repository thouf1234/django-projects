# Generated by Django 3.2.13 on 2022-07-25 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_crud_fdv_model',
            old_name='eadd',
            new_name='author',
        ),
    ]
