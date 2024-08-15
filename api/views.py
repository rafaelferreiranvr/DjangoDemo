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
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            try:
                instance, created = Data.objects.get_or_create(id=0)
                instance.update(request.data)
                return Response(status=status.HTTP_201_CREATED)
            except:
                pass
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
