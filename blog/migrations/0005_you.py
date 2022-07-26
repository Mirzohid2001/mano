# Generated by Django 3.1.14 on 2022-06-26 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='You',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
