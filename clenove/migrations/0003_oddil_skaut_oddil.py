# Generated by Django 4.0.3 on 2022-05-04 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clenove', '0002_alter_skaut_options_skaut_slug_alter_skaut_jmeno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oddil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100, verbose_name='Jméno')),
                ('heslo', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='skaut',
            name='oddil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clenove.oddil', verbose_name='Oddíl'),
        ),
    ]
