# Generated by Django 4.1 on 2022-09-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='max_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results',
            name='min_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='results',
            name='url',
            field=models.CharField(default='url', max_length=100),
        ),
    ]