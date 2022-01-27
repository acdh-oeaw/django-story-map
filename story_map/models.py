from django.db import models

# Create your models here.


class Story(models.Model):
    title = models.CharField(
        max_length=250
    )

    def __str__(self):
        return f"{self.title}"


class Slide(models.Model):
    story = models.ForeignKey(
        'Story',
        on_delete=models.CASCADE,
        related_name="has_slides"
    )
    order_nr = models.PositiveSmallIntegerField(
        help_text="Use this number for ordering your slides"
    )
    location_lat = models.FloatField(
        blank=True,
        null=True
    )
    location_lng = models.FloatField(
        blank=True,
        null=True
    )
    location_zoom = models.PositiveSmallIntegerField(
        default=4
    )
    location_icon_size_l = models.PositiveSmallIntegerField(
        default=48
    )
    location_icon_size_w = models.PositiveSmallIntegerField(
        default=48
    )
    location_line = models.BooleanField(
        default=True
    )
    text_headline = models.CharField(
        max_length=250
    )
    text_text = models.TextField(
        blank=True,
        null=True,
    )
    date = models.DateField(
        blank=True,
        null=True
    )
    media_caption = models.CharField(
        blank=True,
        null=True,
        max_length=250
    )
    media_credit = models.CharField(
        blank=True,
        null=True,
        max_length=250
    )
    media_url = models.URLField(
        blank=True,
        null=True,
        max_length=250
    )

    class Meta:

        ordering = [
            'order_nr',
        ]

    def save(self, *args, **kwargs):
        if self.media_url:
            if self.media_url.startswith('//'):
                self.media_url = self.media_url.replace('//', 'https://')
        super(Slide, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.story.title}__{self.order_nr} {self.text_headline}"

    def location(self):
        item = {
            "iconSize": [
                self.location_icon_size_w, self.location_icon_size_l
            ],
            "lat": self.location_lat,
            "line": self.location_line,
            "lon": self.location_lng,
            "zoom": self.location_zoom
        }
        return item

    def text(self):
        item = {
            "headline": self.text_headline,
            "text": self.text_text
        }
        return item
