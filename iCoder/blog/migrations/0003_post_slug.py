# Generated by Django 5.0.8 on 2024-09-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_contact_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=130),
            preserve_default=False,
        ),
    ]
