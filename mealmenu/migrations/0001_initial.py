# Generated by Django 5.1 on 2024-09-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MealReceipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('method', models.TextField()),
                ('category', models.CharField(choices=[('VEG', 'Vegetarian'), ('NON-VEG', 'Non-Vegetarian')], max_length=10)),
            ],
        ),
    ]
