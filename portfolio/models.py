from django.db import models
from wagtail.core.models import Page
from wagtail.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.images.edit_handlers import ImageChooserPanel
from streamfieldblocks.models import TimelineBlock

from streamfieldblocks.models import ResponsiveImageBlock, SimpleRichTextBlock, CarouselBlock, FlushListBlock


class PortfolioPage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Header background image',
        on_delete=models.SET_NULL,
    )

    headline_text = models.CharField(
        max_length=70,
        blank=True, 
        help_text='Blog listing page header text.'
    )

    experience = StreamField([
        ("Timeline_Block", TimelineBlock()),
    ], null=True, blank=True)

    intro = models.TextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Project Image',
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("background_image"), 
        FieldPanel("headline_text"),
        ImageChooserPanel("image"),
        FieldPanel("intro"),
    ]
 

class ProjectPage(Page):
    project_title = models.CharField(
        max_length=150
    )
    date = models.DateField("Article Date")

    content = StreamField([
        ('richtext', SimpleRichTextBlock()),
        ('carousel', CarouselBlock()),
        ('flush_list', FlushListBlock()),
        ('responsive_image', ResponsiveImageBlock()),
    ], null=True, blank=True)

    testimonials = models.ForeignKey(
        'snippets.Testimonial', 
        on_delete=models.SET_NULL, 
        related_name='+',
        help_text="Project Testimonials",
        blank=True,
        null=True,
    )


    content_panels = Page.content_panels + [
        FieldPanel("project_title"),
        FieldPanel("date"),
        SnippetChooserPanel('testimonials'),
        StreamFieldPanel("content"),
    ]