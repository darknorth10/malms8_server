# Generated by Django 5.0.2 on 2024-04-30 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='mastery',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
    ]
