# Generated by Django 2.2.1 on 2019-06-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0005_example_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='example2',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]