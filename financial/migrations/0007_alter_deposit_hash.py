# Generated by Django 4.1.1 on 2022-09-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0006_alter_deposit_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='hash',
            field=models.CharField(blank=True, help_text='proof of transaction', max_length=1000, null=True, unique=True, verbose_name='Transaction HASH or TXID'),
        ),
    ]