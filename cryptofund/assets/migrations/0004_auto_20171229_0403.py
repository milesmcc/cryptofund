# Generated by Django 2.0 on 2017-12-29 04:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20171229_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a3bf5aad-5f43-4d67-8852-b53782f2bcc8'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1f8c03b0-bc77-46ec-8270-37eb79e13590'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='currency',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('15c02e20-72c4-4b44-acdc-1a0b760632a2'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dollardeposit',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7659397a-6f45-47b1-9e08-e96fef391c3d'), primary_key=True, serialize=False),
        ),
    ]