# Generated by Django 2.1.7 on 2019-04-16 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodBankEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_bank_event', models.CharField(max_length=100)),
                ('food_bank_date', models.DateTimeField(verbose_name='Event Date')),
                ('food_bank_description', models.TextField(blank=True)),
            ],
        ),
    ]
