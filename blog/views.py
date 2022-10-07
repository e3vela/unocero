from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.search.models import Query

from .models import BlogPage, BlogIndexPage


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = BlogPage.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = BlogPage.objects.none()

    # Pagination
    paginator = Paginator(search_results, 9)

    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html", {
            "search_query": search_query,
            "search_results": search_results,
            # There's a single instance of the blog index page
            "blog_index_page": BlogIndexPage.objects.live()[0],
        }
    )
