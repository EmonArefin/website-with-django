# Generated by Django 4.1.7 on 2023-03-28 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
