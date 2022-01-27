import requests
from story_map.models import Slide, Story


def fetch_data_from_knightlab(url):
    r = requests.get(url)
    return r.json()


def slides_from_knightlab_data(data):
    return data['storymap']['slides']


def save_slides(slides, story_title='default story'):
    story, _ = Story.objects.get_or_create(title=story_title)
    story.has_slides.all().delete()
    items = []
    for i, x in enumerate(slides):
        order_nr = i + 1
        item = Slide.objects.create(
            story=story,
            order_nr=order_nr,
            text_headline=x['text']['headline'],
            media_caption=x['media']['caption'],
            media_credit=x['media']['credit'],
            media_url=x['media']['url'],
        )
        try:
            item.text_text = x['text']['text']
        except KeyError:
            pass
        try:
            item.location_lat = x['location']['lat']
            item.location_lng = x['location']['lon']
        except KeyError:
            pass
        item.save()
        items.append(item)
    return(items)


def import_from_knlab(url, story_title):
    data = fetch_data_from_knightlab(url)
    slides = slides_from_knightlab_data(data)
    items = save_slides(slides, story_title)
    return items
