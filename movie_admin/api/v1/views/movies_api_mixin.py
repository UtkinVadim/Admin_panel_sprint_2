from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from movies.models import Filmwork, RoleType


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ["get"]

    def get_queryset(self):
        actors = ArrayAgg(
            "persons__full_name",
            filter=Q(persons__personfilmwork__role=RoleType.actor),
            distinct=True,
        )
        directors = ArrayAgg(
            "persons__full_name",
            filter=Q(persons__personfilmwork__role=RoleType.director),
            distinct=True,
        )
        writers = ArrayAgg(
            "persons__full_name",
            filter=Q(persons__personfilmwork__role=RoleType.writer),
            distinct=True,
        )
        genres = ArrayAgg("genres__name", distinct=True)
        return (
            self.model.objects.prefetch_related("genres", "persons")
            .values("id", "title", "description", "creation_date", "rating", "type")
            .annotate(
                actors=actors,
                directors=directors,
                writers=writers,
                genres=genres,
            )
            .order_by("title")
        )

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
