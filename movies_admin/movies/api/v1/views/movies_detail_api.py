from django.views.generic.detail import BaseDetailView
from .movies_api_mixin import MoviesApiMixin


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    pk_url_kwarg = "id"

    def get_context_data(self, **film_data):
        return film_data.get("object")
