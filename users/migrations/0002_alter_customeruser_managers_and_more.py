# Generated by Django 5.1.2 on 2024-10-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
