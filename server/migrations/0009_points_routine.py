# Generated by Django 2.2.5 on 2020-12-04 13:30

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('server', '0008_auto_20201204_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', djongo.models.fields.JSONField()),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Routine')),
            ],
        ),
    ]
