from rest_framework import serializers
from otgalbum.models import Gromada

class GromadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gromada
        fields = '__all__'