# Generated by Django 4.2.3 on 2023-07-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_citizen_cep_alter_city_cep_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrence',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
