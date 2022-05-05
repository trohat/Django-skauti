# Generated by Django 4.0.3 on 2022-05-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clenove', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skaut',
            options={'verbose_name_plural': 'Skauti'},
        ),
        migrations.AddField(
            model_name='skaut',
            name='slug',
            field=models.SlugField(default='nic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skaut',
            name='jmeno',
            field=models.CharField(max_length=100, verbose_name='Jméno'),
        ),
        migrations.AlterField(
            model_name='skaut',
            name='prezdivka',
            field=models.CharField(help_text='Prosím, zadávejte bez diakritiky', max_length=100, verbose_name='Přezdívka'),
        ),
        migrations.AlterField(
            model_name='skaut',
            name='splneno',
            field=models.BooleanField(default=False, help_text='Už splnil skautskou zkoušku?', verbose_name='Splněno'),
        ),
        migrations.AlterField(
            model_name='skaut',
            name='vek',
            field=models.IntegerField(verbose_name='Věk'),
        ),
    ]
