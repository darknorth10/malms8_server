# Generated by Django 5.0.2 on 2024-04-24 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_assessment_module_masterylevel_score'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Module',
        ),
    ]