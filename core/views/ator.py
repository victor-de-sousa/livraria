from rest_framework.viewsets import ModelViewSet;

from core.serializers import AtorSerializer;
from core.models import Ator;

class AtorViewSet(ModelViewSet):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer