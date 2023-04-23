from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .models import Asset
from .fetch_assets import fetch_assets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from assets.serializers.common import AssetSerializer


class GetAllAssetsView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request):
        
        #to populate all assets into the DB from API . Can change how many with format ('US')[0:n] n is int
        #fetch_assets()
        
        assets = Asset.objects.all()
        serialized_assets = AssetSerializer(assets, many=True)
        return Response({"All Asset Data": serialized_assets.data})