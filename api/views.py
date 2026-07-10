from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from .serializers import CarSerializer
from showroom.models import Car

# class CarListAPIView(APIView):
#     def get(self,request):
#         cars=Car.objects.all()
#         serializer=CarSerializer(cars,many=True)
#         return Response(serializer.data)
    

#     def post(self,request):
#         serializer=CarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

# class CarListCreateAPIView(generics.ListCreateAPIView):
#     queryset=Car.objects.all()
#     serializer_class=CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset=Car.objects.all()
    serializer_class=CarSerializer