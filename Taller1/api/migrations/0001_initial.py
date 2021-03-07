# Generated by Django 3.1.7 on 2021-03-07 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('identifier', models.AutoField(primary_key=True, serialize=False)),
                ('artist_id', models.CharField(max_length=255)),
                ('artist_name', models.CharField(max_length=255)),
                ('track_name', models.CharField(max_length=255)),
                ('track_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=60, unique=True)),
                ('identifier', models.AutoField(primary_key=True, serialize=False)),
                ('is_old_user', models.BooleanField(default=False)),
                ('recommendation_frame', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Interactions',
            fields=[
                ('identifier', models.AutoField(primary_key=True, serialize=False)),
                ('artist_id', models.CharField(max_length=255)),
                ('artist_name', models.CharField(max_length=255)),
                ('track_name', models.CharField(max_length=255)),
                ('track_id', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('is_explicit', models.BooleanField(default=False)),
                ('count', models.PositiveIntegerField()),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
