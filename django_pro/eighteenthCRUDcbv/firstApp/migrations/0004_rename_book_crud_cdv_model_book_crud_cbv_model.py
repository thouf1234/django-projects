# Generated by Django 3.2.13 on 2022-07-25 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_rename_book_crud_fdv_model_book_crud_cdv_model'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='book_crud_cdv_model',
            new_name='book_crud_cbv_model',
        ),
    ]