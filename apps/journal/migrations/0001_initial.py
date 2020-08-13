# Generated by Django 3.1 on 2020-08-13 07:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('is_public', models.BooleanField(default=False, verbose_name='Is public')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Rating')),
                ('energy', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Energy (kcal/kg/min)')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('is_public', models.BooleanField(default=False, verbose_name='Is public')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Rating')),
                ('energy', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Energy (kcal)')),
                ('protein', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Protein (gr)')),
                ('carbohydrate', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Carbohydrate (gr)')),
                ('fat', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Fat (gr)')),
                ('fiber', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Fiber (gr)')),
                ('sugar', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Sugar (gr)')),
                ('salt', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Salt (gr)')),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='FoodPortion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('is_public', models.BooleanField(default=False, verbose_name='Is public')),
                ('weight', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Weight (gr)')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Food portion',
                'verbose_name_plural': 'Food portions',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='FoodJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Weight (gr)')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Datetime')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.food')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Food journal',
                'verbose_name_plural': 'Food journal',
                'ordering': ['datetime'],
            },
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('is_public', models.BooleanField(default=False, verbose_name='Is public')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('portions', models.ManyToManyField(related_name='Portions', to='journal.FoodPortion')),
            ],
            options={
                'verbose_name': 'Food category',
                'verbose_name_plural': 'Food categories',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='journal.foodcategory'),
        ),
        migrations.AddField(
            model_name='food',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ActivityJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Duration (min)')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Datetime')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.activity')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity journal',
                'verbose_name_plural': 'Activity journal',
                'ordering': ['datetime'],
            },
        ),
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('is_public', models.BooleanField(default=False, verbose_name='Is public')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity category',
                'verbose_name_plural': 'Activity categories',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='journal.activitycategory'),
        ),
        migrations.AddField(
            model_name='activity',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
