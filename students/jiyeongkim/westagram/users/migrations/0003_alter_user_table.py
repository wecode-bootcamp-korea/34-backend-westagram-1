# Generated by Django 4.0.5 on 2022-06-11 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]