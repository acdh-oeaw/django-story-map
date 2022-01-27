from django.views.generic.detail import DetailView


from . models import Story


class StoryDetailView(DetailView):
    model = Story
    template_name = 'story_map/story_detail.html'
