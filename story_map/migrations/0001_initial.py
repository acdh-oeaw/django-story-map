# Generated by Django 3.2.11 on 2022-01-27 12:45

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
                ('attribution', models.CharField(blank=True, max_length=250, null=True)),
                ('call_to_action', models.BooleanField(default=True)),
                ('call_to_action_text', models.CharField(blank=True, max_length=250, null=True)),
                ('language', models.CharField(default='en', max_length=2)),
                ('map_background_color', models.CharField(default='#5f9468', max_length=15)),
                ('map_subdomains', models.CharField(blank=True, max_length=25, null=True)),
                ('map_type', models.CharField(blank=True, max_length=25, null=True)),
                ('zoomify_path', models.CharField(blank=True, max_length=250, null=True)),
                ('zoomify_height', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('zoomify_width', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('zoomify_attribution', models.CharField(blank=True, max_length=250, null=True)),
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
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_slides', to='story_map.story')),
            ],
            options={
                'ordering': ['order_nr'],
            },
        ),
    ]
