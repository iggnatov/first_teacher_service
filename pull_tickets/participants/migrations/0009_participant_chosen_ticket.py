# Generated by Django 4.2.4 on 2023-08-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0008_remove_participant_chosen_ticket_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='chosen_ticket',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]