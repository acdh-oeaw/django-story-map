# Generated by Django 3.2.11 on 2022-01-27 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_nr', models.PositiveSmallIntegerField(help_text='Use this number for ordering your slides')),
                ('location_lat', models.FloatField(blank=True, null=True)),
                ('location_lng', models.FloatField(blank=True, null=True)),
                ('location_zoom', models.PositiveSmallIntegerField(default=4)),
                ('location_icon_size_l', models.PositiveSmallIntegerField(default=48)),
                ('location_icon_size_w', models.PositiveSmallIntegerField(default=48)),
                ('location_line', models.BooleanField(default=True)),
                ('text_headline', models.CharField(max_length=250)),
                ('text_text', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('media_caption', models.CharField(blank=True, max_length=250, null=True)),
                ('media_credit', models.CharField(blank=True, max_length=250, null=True)),
                ('media_url', models.URLField(blank=True, max_length=250, null=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story_map.story')),
            ],
            options={
                'ordering': ['order_nr'],
            },
        ),
    ]
