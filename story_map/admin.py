from django.contrib import admin
from story_map.models import Story, Slide


@admin.register(Slide)
class RecogitoAdmin(admin.ModelAdmin):
    list_display = (
        "order_nr",
        "story",
        "text_headline",
    )
    list_filter = (
        "story",
    )


@admin.register(Story)
class SlideAdmin(admin.ModelAdmin):
    pass
