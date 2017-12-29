# Generated by Django 2.0 on 2017-12-29 05:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20171229_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7b62bb5c-f3c1-46ae-8e3e-5112fd9e81ac'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='access_code',
            field=models.CharField(default='8BHVVPCE', max_length=8),
        ),
        migrations.AlterField(
            model_name='client',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8a40809b-2da4-4c13-ab93-45618dd266e3'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='currency',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('5f966d72-9367-4b32-8006-6f2a804c8e07'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dollardeposit',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('13271f0a-7c8e-4d5f-9ecf-827f62d5d500'), primary_key=True, serialize=False),
        ),
    ]
