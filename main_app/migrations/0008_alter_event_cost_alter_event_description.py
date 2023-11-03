# Generated by Django 4.2.7 on 2023-11-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_event_user_alter_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Please enter the amount as a number without the "$" symbol, e.g., 0.00 or 0', max_digits=8),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
