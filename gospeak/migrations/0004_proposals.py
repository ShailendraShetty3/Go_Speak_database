# Generated by Django 4.0.3 on 2024-06-19 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gospeak', '0003_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposals',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('speakers', models.CharField(max_length=100)),
                ('event_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=15)),
                ('cfp_id', models.ForeignKey(db_column='cfp_id', on_delete=django.db.models.deletion.CASCADE, to='gospeak.cfps')),
                ('talk_id', models.ForeignKey(db_column='group_id', on_delete=django.db.models.deletion.CASCADE, to='gospeak.groups')),
            ],
        ),
    ]
