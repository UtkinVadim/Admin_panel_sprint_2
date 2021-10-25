from api.v1.views.movies_api_mixin import MoviesApiMixin
from django.views.generic.detail import BaseDetailView


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    pk_url_kwarg = "id"

    def get_context_data(self, **film_data):
        return film_data.get("object")
