# Generated by Django 4.2.4 on 2023-08-25 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0004_alter_participant_chosen_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='chosen_date',
        ),
    ]
