from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class SiteSetting(BaseSetting):
    """
    Setting for storing site-wide variables
    """

    logo = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+"
    )
    featured_blog_page = models.ForeignKey(
        "blog.BlogPage", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="featured_blog_post",
        help_text="Featured blog post right above footer",
    )
    footer_content = RichTextField(blank=True)

    panels = [
        ImageChooserPanel("logo"),
        FieldPanel("featured_blog_page"),
        FieldPanel("footer_content"),
    ]

    class Meta:
        verbose_name = "site settings"


class RichTextPage(Page):
    date = models.DateField("Post date")
    body = StreamField([
        ("heading", blocks.CharBlock(form_classname="full title")),
        ("paragraph", blocks.RichTextBlock()),
        ("image", ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        StreamFieldPanel("body"),
    ]

    def get_context(self, request):
        context = super(RichTextPage, self).get_context(request)

        site_settings = SiteSetting.for_request(request)

        context["blog_index_page"] = self.get_parent().specific
        context["featured_posts"] = [site_settings.featured_blog_page]

        return context
