from core import models, serializers

import django_filters
from rest_framework import viewsets


class ToolView(viewsets.ModelViewSet):

    serializer_class = serializers.ToolSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        'created': ('lt', 'gt'),
        'updated': ('lt', 'gt'),
        'name': ('exact', 'contains'),
        'value': ('exact',),
    }
    ordering_fields = (
        'created',
    )

    def get_queryset(self):
        return models.Tool.objects.all()
