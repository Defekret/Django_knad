# Generated by Django 4.1.7 on 2023-03-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='phones/default.png', upload_to='phones/')),
                ('model_name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('color', models.CharField(max_length=200)),
                ('operation_system', models.CharField(max_length=200)),
                ('screen_size', models.FloatField()),
                ('preview_text', models.TextField()),
                ('rating', models.IntegerField()),
                ('camera_resolution', models.FloatField()),
                ('stock_quantity', models.IntegerField()),
            ],
        ),
    ]