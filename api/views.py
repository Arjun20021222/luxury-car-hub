from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from .serializers import CarSerializer,StudentSerializer,RegisterSerializer
from showroom.models import Car
from student.models import Student
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter
from rest_framework.filters import SearchFilter,OrderingFilter

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
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_class=CarFilter
    search_fileds=[
        "brand",
        "model",
        "color",
        "fuel_type",
        "transmission",
        "description",
    ]

    ordering_fileds=[
        "price",
        "year",
        "brand",
        "created_at",
    ]

    ordering=["-created_at"]
    

class StudentApiView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        

class RegisterApiView(generics.CreateAPIView):
    serializer_class=RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message":"User registered successfully"
        },status=status.HTTP_201_CREATED)
    
