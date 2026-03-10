from rest_framework.serializers import ModelSerializer

from core.models import Ator

class AtorSerializer(ModelSerializer):
    model = Ator
    fields = '__all__'