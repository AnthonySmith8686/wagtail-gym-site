from django.db import models
from wagtail.blocks import StructBlock

# Create your models here.
class SEOSettings(StructBlock):
    page_title = models.CharField(max_length=255)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    default_canonical_url = models.URLField(blank=True)
    default_robots_meta_tags = models.CharField(max_length=255, blank=True)