# Generated by Django 4.2.2 on 2023-07-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_citizen_cep_alter_citizen_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='cep',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='city',
            name='cep',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='cep',
            field=models.IntegerField(),
        ),
    ]
