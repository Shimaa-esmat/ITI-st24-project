# Generated by Django 5.1.2 on 2024-10-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
