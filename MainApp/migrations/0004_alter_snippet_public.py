# Generated by Django 4.2.7 on 2023-12-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_snippet_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
