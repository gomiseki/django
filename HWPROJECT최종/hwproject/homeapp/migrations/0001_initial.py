# Generated by Django 3.0.8 on 2020-07-21 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor', models.CharField(max_length=50)),
                ('rq_year', models.IntegerField()),
                ('rq_semester', models.IntegerField()),
                ('department', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('instruction_number', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('credit', models.IntegerField()),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('rating', models.IntegerField()),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.Lecture')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
