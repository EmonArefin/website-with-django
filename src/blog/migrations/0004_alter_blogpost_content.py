# Generated by Django 4.1.7 on 2023-03-25 09:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_options_blogpost_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
