from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from movies.models import Filmwork, RoleType


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ["get"]

    def get_queryset(self):
        genres = ArrayAgg("genres__name", distinct=True)
        return (
            self.model.objects.prefetch_related("genres", "persons")
            .values("id", "title", "description", "creation_date", "rating", "type")
            .annotate(
                actors=self._aggregate_person(role=RoleType.actor),
                directors=self._aggregate_person(role=RoleType.director),
                writers=self._aggregate_person(role=RoleType.writer),
                genres=genres,
            )
            .order_by("title")
        )

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)

    def _aggregate_person(self, role: str):
        return ArrayAgg(
            "persons__full_name",
            filter=Q(persons__personfilmwork__role=role),
            distinct=True,
        )
