from rest_framework import serializers
from .models import Ghar

class GharSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ghar
        fields = ('name','floors','location', 'owner')