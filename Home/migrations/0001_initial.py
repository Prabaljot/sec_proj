# Generated by Django 4.2.4 on 2023-09-03 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=20)),
                ('msg', models.TextField()),
                ('dateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
