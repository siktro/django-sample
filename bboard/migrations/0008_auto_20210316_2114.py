# Generated by Django 3.1.7 on 2021-03-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0007_bb_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='kind',
            field=models.CharField(blank=True, choices=[('Купить', 'Купить'), ('Продать', 'Продать'), ('Объменять', 'Объменять')], max_length=10),
        ),
    ]
