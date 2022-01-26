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
    )
    order_nr = models.PositiveSmallIntegerField(
        help_text="Use this number for ordering your slides"
    )
    lat = models.FloatField(
        blank=True,
        null=True
    )
    lng = models.FloatField(
        blank=True,
        null=True
    )
    zoom = models.PositiveSmallIntegerField(
        default=4
    )
    line = models.BooleanField(
        default=True
    )
    headline = models.CharField(
        max_length=250
    )
    text = models.TextField(
        blank=True,
        null=True,
    )
    date = models.DateField(
        blank=True,
        null=True
    )

    class Meta:

        ordering = [
            'order_nr',
        ]

    def __str__(self):
        return f"{self.headline} ({self.order_nr}"
