# Generated by Django 5.0.2 on 2024-04-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_useraccount_mastery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='type_of',
            field=models.CharField(choices=[('formative', 'FORMATIVE'), ('mastery', 'MASTERY'), ('post_test', 'POST-TEST'), ('pre_test', 'PRE-TEST')], max_length=50),
        ),
    ]