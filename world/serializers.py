from rest_framework import serializers
from rest_framework.serializers import StringRelatedField,ModelSerializer
from .models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer
class EvacuationSerializer(GeoFeatureModelSerializer):

    class Meta:
        model=Evacuation
        fields=('id','evacuation_site','location','geom',)
        geo_field=('geom')


class EvacuationDetailSerializer(ModelSerializer):
    evacuation_site=StringRelatedField()
    
    class Meta:
        model=Evacuation
        fields=('evacuation_site','location',)
    

class CitySerializer(ModelSerializer):

    class Meta:
        model=City
        fields=('id','code','name',)

class PrefSerializer(ModelSerializer):

    class Meta:
        model=Pref
        fields=('id','name',)

class FormSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=('evacuation_pk','memo',)