from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from . import serializers
from . import models
from rest_framework.response import Response


class QuestLeafViewSet(viewsets.ModelViewSet):
    queryset = models.QuestLeaf.objects.all()
    serializer_class = serializers.QuestLeafSerializer

    @action(detail=True, methods=['patch'])
    def add_next(self, request, pk=None):
        next_leaf = get_object_or_404(models.QuestLeaf, pk=request.data.get('next_id'))
        leaf = self.get_object()
        leaf.next.add(next_leaf)
        return Response(str(next_leaf.id) + "added")

    @action(detail=True, methods=['patch'])
    def remove_next(self, request, pk=None):
        next_leaf = get_object_or_404(models.QuestLeaf, pk=request.data.get('next_id'))
        leaf = self.get_object()
        leaf.next.remove(next_leaf)
        return Response(str(next_leaf.id) + "removed")


class ParamViewSet(viewsets.ModelViewSet):
    queryset = models.Param.objects.all()
    serializer_class = serializers.ParamSerializer


class ParamsSetViewSet(viewsets.ModelViewSet):
    queryset = models.ParamsSet.objects.all()
    serializer_class = serializers.ParamsSetSerializer

