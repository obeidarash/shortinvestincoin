# Generated by Django 4.1.1 on 2022-10-15 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_news_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=512, unique=True),
        ),
    ]
