# Generated by Django 4.0.6 on 2022-08-11 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricetable',
            old_name='pt_newPtice',
            new_name='pt_newPrice',
        ),
    ]
