# Generated by Django 2.2.1 on 2019-07-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0006_example2_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='img',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
