# Generated by Django 4.2.1 on 2023-06-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_usermodel_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]