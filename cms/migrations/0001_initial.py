# Generated by Django 4.0.6 on 2022-08-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cms_img', models.ImageField(upload_to='sliderimg/')),
                ('cms_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('cms_text', models.CharField(max_length=200, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
