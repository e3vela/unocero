from django.db import models
from django.core.paginator import Paginator
from django.utils.text import slugify

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from theme.models import SiteSetting


class BlogIndexPage(RoutablePageMixin, Page):

    max_count = 1
    ajax_template = "blog/includes/blog_tile.html"

    def get_posts(self):
        """
        Retrieve all live blog posts
        """

        # Live posts ordered by reverse-chron
        return (
            BlogPage.objects.descendant_of(self)
            .live().order_by("-first_published_at")
        )

    def paginate_posts(self, posts, request, begin_from, n_posts):
        """
        Show desired blog posts when requesting from Ajax
        """

        is_paginated = False
        can_paginate = False

        if request.is_ajax():
            # Begin from the posts which are not yet shown
            posts = posts[begin_from:]

            paginator = Paginator(posts, n_posts)
            page = int(request.GET.get("page"))

            if page <= paginator.num_pages:
                posts = paginator.page(page)

                is_paginated = True
                can_paginate = posts.has_next()
            else:
                posts = None

        else:
            # Request is not from Ajax, it is most probaly the
            # first page, return the first posts to show
            can_paginate = len(posts) > begin_from
            posts = posts[:begin_from]

        return posts, can_paginate, is_paginated

    @route("^$")
    def all_posts(self, request):
        """
        Obtain all blog posts
        """

        # Default number of posts to show when page loads
        # and how many to show when loading with ajax
        n_posts = 9
        n_injected_posts = 6

        # Make sure to only show blog pages
        posts = [
            post for post in self.get_posts()
            if isinstance(post.specific, BlogPage)
        ]

        # Paginate and obtain information if pagination is possible
        posts, can_paginate, is_paginated = self.paginate_posts(
            posts, request, begin_from=n_posts, n_posts=n_injected_posts)

        return self.render(
            request,
            context_overrides={
                "blog_index_page": self,
                "posts": posts,
                # When not showing paginated posts, show blog posts on a
                # featured view
                "featured_display": not is_paginated,
                "can_paginate": can_paginate,
                "is_paginated": is_paginated,
            }
        )

    @route(r"^category/(?P<slug>[-\w]+)/$", name="category_index")
    def posts_by_category(self, request, slug=None):
        """
        Obtain all blog posts for a certain category
        """

        n_posts = 6
        n_injected_posts = 6

        posts = self.get_posts().filter(category__slug=slug)

        # Paginate and obtain information if pagination is possible
        posts, can_paginate, is_paginated = self.paginate_posts(
            posts, request, begin_from=n_posts, n_posts=n_injected_posts)

        return self.render(
            request,
            context_overrides={
                "blog_index_page": self,
                "posts": posts,
                "category_name": slug,
                "can_paginate": can_paginate,
                "is_paginated": is_paginated,
            }
        )

    class Meta:
        verbose_name = "blog index page"


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    category = models.ForeignKey(
        "BlogCategory", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="blog_category",
    )
    main_image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+"
    )

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("date"),
            FieldPanel("category"),
        ], heading="Blog information"),
        FieldPanel("intro"),
        FieldPanel("body"),
        ImageChooserPanel("main_image"),
    ]

    def get_context(self, request):
        context = super(BlogPage, self).get_context(request)

        site_settings = SiteSetting.for_request(request)

        context["blog_index_page"] = self.get_parent().specific
        context["featured_posts"] = [site_settings.featured_blog_page]

        return context

    class Meta:
        verbose_name = "blog page"
        verbose_name_plural = "blog pages"


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    panels = [
        FieldPanel("name"),
    ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(BlogCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "blog category"
        verbose_name_plural = "blog categories"
