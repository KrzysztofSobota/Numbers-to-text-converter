# Generated by Django 3.0.2 on 2020-01-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liczby_tekst', '0002_auto_20200107_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changeinput',
            name='numbers',
            field=models.IntegerField(max_length=15),
        ),
    ]
