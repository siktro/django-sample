# Generated by Django 3.1.7 on 2021-03-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_auto_20210316_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
