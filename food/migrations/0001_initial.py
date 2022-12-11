# Generated by Django 3.1 on 2022-12-04 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Food Name')),
                ('calories', models.FloatField(verbose_name='Calories (kcal)')),
                ('total_fat', models.FloatField(verbose_name='Total Fat (g)')),
                ('saturated_fat', models.FloatField(verbose_name='Saturated Fat (g)')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serving_size', models.IntegerField(verbose_name='Serving Size')),
                ('meal_time', models.IntegerField(choices=[(1, 'Breakfast'), (2, 'Lunch')], verbose_name='Meal Time')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food', verbose_name='Food')),
            ],
        ),
    ]
