from rest_framework import viewsets


from api.marketplaces.serializers import MarketplacesModelSerializer
from marketplaces.models import MarketPlace


class MarketplacesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = MarketPlace.objects.all()
    serializer_class = MarketplacesModelSerializer
    permission_classes = []
