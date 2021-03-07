# Generated by Django 3.1.7 on 2021-03-07 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210303_1627'),
    ]

    operations = [
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
        migrations.DeleteModel(
            name='interaction',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='count',
        ),
    ]
