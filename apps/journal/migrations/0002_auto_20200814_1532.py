# Generated by Django 3.1 on 2020-08-14 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calorie_api', '0002_auto_20200814_1532'),
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitycategory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='food',
            name='category',
        ),
        migrations.RemoveField(
            model_name='food',
            name='portions',
        ),
        migrations.RemoveField(
            model_name='food',
            name='user',
        ),
        migrations.RemoveField(
            model_name='foodcategory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='foodportion',
            name='user',
        ),
        migrations.AlterField(
            model_name='activityjournal',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calorie_api.activity'),
        ),
        migrations.AlterField(
            model_name='foodjournal',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calorie_api.food'),
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='ActivityCategory',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='FoodCategory',
        ),
        migrations.DeleteModel(
            name='FoodPortion',
        ),
    ]
