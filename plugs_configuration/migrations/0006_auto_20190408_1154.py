# Generated by Django 2.1.7 on 2019-04-08 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plugs_configuration', '0005_auto_20170913_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
