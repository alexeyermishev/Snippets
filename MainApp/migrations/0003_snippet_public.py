# Generated by Django 4.2.7 on 2023-12-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_snippet_user_alter_snippet_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='public',
            field=models.CharField(choices=[('public', True), ('notpublic', False)], default=True, max_length=10),
            preserve_default=False,
        ),
    ]
