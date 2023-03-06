# Generated by Django 4.1.5 on 2023-01-03 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='m_team',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=300, unique=True)),
                ('coach', models.CharField(default=None, max_length=300, null=True)),
                ('captain', models.CharField(default=None, max_length=300, null=True)),
                ('stadium', models.CharField(default=None, max_length=300, null=True)),
                ('location', models.CharField(default=None, max_length=300, null=True)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='m_match',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('score1', models.IntegerField(default=0)),
                ('score2', models.IntegerField(default=0)),
                ('start_time_tz', models.DateTimeField(default=None, null=True)),
                ('end_time_tz', models.DateTimeField(default=None, null=True)),
                ('team1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_team1', to='matches.m_team')),
                ('team2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_team2', to='matches.m_team')),
            ],
        ),
    ]