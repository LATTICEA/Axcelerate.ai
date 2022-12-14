# Generated by Django 4.1.4 on 2022-12-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blogmodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=1000)),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upload_to', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(upload_to='blog')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
