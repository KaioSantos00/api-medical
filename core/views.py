from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer