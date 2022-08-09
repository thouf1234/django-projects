# Generated by Django 3.2.13 on 2022-07-29 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('esal', models.FloatField()),
                ('eadd', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ProxyEmployee1',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('firstApp.employee',),
        ),
        migrations.CreateModel(
            name='ProxyEmployee2',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('firstApp.employee',),
        ),
    ]