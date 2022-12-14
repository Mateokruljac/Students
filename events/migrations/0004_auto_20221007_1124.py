# Generated by Django 3.2.11 on 2022-10-07 09:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_bio',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Image'),
        ),
    ]
