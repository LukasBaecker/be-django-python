# Generated by Django 4.0.5 on 2022-06-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
