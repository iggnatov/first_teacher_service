# Generated by Django 4.2.4 on 2023-08-25 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0008_remove_participant_chosen_ticket_and_more'),
        ('tickets', '0004_ticket_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='participant',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='participants.participant', to_field='code_for_link'),
        ),
    ]