# Generated by Django 4.1.4 on 2022-12-14 09:35

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
