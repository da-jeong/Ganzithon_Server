# Generated by Django 4.2.7 on 2023-11-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='day_num',
            field=models.IntegerField(null=True),
        ),
    ]
