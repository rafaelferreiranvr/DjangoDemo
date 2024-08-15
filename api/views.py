from rest_framework.views import APIView, status
from rest_framework.response import Response
from .serializers import DataSerializer
from .models import Data

class DataAPIView(APIView):
    def get(self, request):
        instance, created = Data.objects.get_or_create(id=0)
        data = DataSerializer(instance).data
        return Response(status=status.HTTP_200_OK, data=data)

    def post(self, request):
        print()