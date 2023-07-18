from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from team.models import TeamMember
from seo.models import SEOSettings

class ContentPage(Page):
    content = StreamField([
        ('hero', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('subtitle', blocks.CharBlock()),
            ('image', ImageChooserBlock(required=False)),
    ])),
        ('centered_text', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('text', blocks.RichTextBlock()),
            ])),
        ('team_members', blocks.ListBlock(SnippetChooserBlock(TeamMember), icon="user"))
    ], use_json_field=True, blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

    api_fields = [
        APIField('content'),
    ]