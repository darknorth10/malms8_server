# Generated by Django 5.0.2 on 2024-04-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_question_delete_masterylevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='mastery',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]