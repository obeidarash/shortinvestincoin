# Generated by Django 4.1 on 2022-08-12 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('access_token', '0003_accesstoken_representative'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(default=1, help_text='belongs to 3 different user', on_delete=django.db.models.deletion.CASCADE, related_name='test_id', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
