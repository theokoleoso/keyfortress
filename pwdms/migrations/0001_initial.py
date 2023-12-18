# Generated by Django 5.0 on 2023-12-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(max_length=128)),
                ('website_url', models.URLField(max_length=256)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(blank=True, max_length=64, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
