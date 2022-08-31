# Generated by Django 4.1 on 2022-08-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0003_alter_deposit_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='hash',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True, verbose_name='Transaction HASH or TXID'),
        ),
    ]