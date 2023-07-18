from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
        FieldPanel('bio'),
    ]

    def __str__(self):
        return self.name