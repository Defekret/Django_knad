# Generated by Django 4.1.7 on 2023-03-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='storage',
            field=models.IntegerField(default=128),
        ),
    ]
