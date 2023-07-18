from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet

@register_snippet
class Menu(models.Model):
    name = models.CharField(max_length=50, blank=True)
    menu_items = StreamField([
        ('navigation_links', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('link', blocks.CharBlock()),
        ])),
    ], use_json_field=True, blank=True)


    panels = [
        FieldPanel('name'),
        FieldPanel('menu_items'),
    ]

    def __str__(self):
        return self.name
