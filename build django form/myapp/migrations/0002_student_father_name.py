# Generated by Django 4.2.8 on 2023-12-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.TextField(default='Hamed'),
        ),
    ]
