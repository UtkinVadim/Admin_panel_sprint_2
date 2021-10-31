from django.views.generic.list import BaseListView

from .movies_api_mixin import MoviesApiMixin


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            self.get_queryset(), self.paginate_by
        )
        previous_page_number = (
            page.previous_page_number() if page.has_previous() else None
        )
        next_page_number = page.next_page_number() if page.has_next() else None

        context = {
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "prev": previous_page_number,
            "next": next_page_number,
            "results": list(queryset),
        }
        return context
