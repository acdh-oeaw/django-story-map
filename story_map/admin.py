from django.contrib import admin
from story_map.models import Story, Slide


@admin.register(Slide)
class RecogitoAdmin(admin.ModelAdmin):
    list_display = (
        "story",
        "headline",
        "order_nr",
    )
    list_filter = (
        "story",
    )


@admin.register(Story)
class SlideAdmin(admin.ModelAdmin):
    pass
