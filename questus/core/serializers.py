from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ShortLeafSerializer(serializers.ModelSerializer):

    id = serializers.PrimaryKeyRelatedField(queryset=QuestLeaf.objects.all())
    class Meta:
        model = QuestLeaf
        fields = ('id', 'text')


class QuestLeafSerializer(serializers.ModelSerializer):
    next = ShortLeafSerializer(many=True, required=False)

    class Meta:
        model = QuestLeaf
        fields = '__all__'

    def update(self, instance, validated_data):
        for obj in validated_data.get('next'):
            instance.next.add(obj.get('id'))

        instance.save()
        return instance

class ParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Param
        fields = '__all__'


class ParamsSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParamsSet
        fields = '__all__'
