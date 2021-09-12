from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from django.db.models import Q
from django.contrib.postgres.aggregates import ArrayAgg

from movies.models import FilmWork


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ['get']

    @staticmethod
    def get_queryset():
        qs = FilmWork.objects.values('id', 'title', 'description', 'creation_date', 'rating', 'type'
                ).annotate(
                    genres=ArrayAgg('genres__name', distinct=True)
                ).annotate(
                    actors=ArrayAgg('personfilmwork__person__full_name',
                        filter=Q(personfilmwork__role='actor'), distinct=True),
                    directors=ArrayAgg('personfilmwork__person__full_name',
                        filter=Q(personfilmwork__role='director'), distinct=True),
                    writers=ArrayAgg('personfilmwork__person__full_name',
                        filter=Q(personfilmwork__role='writer'), distinct=True))
        return qs

    @staticmethod
    def render_to_response(context, **response_kwargs):
        return JsonResponse(context)


class Movies(MoviesApiMixin, BaseListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        paginate_by = 50
        queryset = list(self.get_queryset())
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            paginate_by
        )
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': queryset,
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):

    def get_context_data(self, **kwargs):
        context = {
            'results': list(kwargs.values()),
        }
        return context
