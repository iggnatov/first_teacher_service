# Generated by Django 4.2.4 on 2023-08-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0007_alter_participant_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='chosen_ticket',
        ),
        migrations.AlterField(
            model_name='participant',
            name='code_for_link',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
