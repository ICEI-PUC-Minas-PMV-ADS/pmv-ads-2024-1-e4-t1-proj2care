from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Greeting, Caregiver, Specialization
from .serializers import GreetingSerializer, CaregiverSerializer

class GreetingList(APIView):
    def get(self, request):
        greetings = Greeting.objects.all()
        serializer = GreetingSerializer(greetings, many=True)
        return Response(serializer.data)


class CaregiverList(generics.ListAPIView): #Não sei se essa url faz sentido já que vamos pegar do mongo, mas como não temos mongo ainda, ta ai.
    queryset = Caregiver.objects.all()  #lembrando que tem que implementar filtro tbm {query_params} quando passar pro mongo.
    serializer_class = CaregiverSerializer
    permission_classes = (AllowAny,) #fixme precisa do user pra auth

class CaregiverEdit(APIView):
    queryset = Caregiver.objects.all()
    serializer_class = CaregiverSerializer
    permission_classes = (AllowAny,) #fixme precisa do user pra auth

    #como não temos a token ainda, não consigo direcionar pro usuario certo
    def put(self, request, format=None):
        caregiver = self.queryset.first()  #fixme

        serializer = CaregiverSerializer(caregiver, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        caregiver = self.queryset.first()  #fixme
        serializer = CaregiverSerializer(caregiver, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaregiverSelfCalendarView(generics.RetrieveAPIView):
    queryset = Caregiver.objects.all()
    serializer_class = CaregiverSerializer
    permission_classes = (AllowAny,) #fixme precisa do user pra auth

    def retrieve(self, request, *args, **kwargs):
        instance = self.queryset.first() #fixme
        serializer = self.get_serializer(instance)

        calendar = {
           "fixed_unavailable_days":serializer.data.get('fixed_unavailable_days', []),
           "fixed_unavailable_hours":serializer.data.get('fixed_unavailable_hours', []),
           "custom_unavailable_days":serializer.data.get('custom_unavailable_days',[])
        }

        return Response(calendar)

class CaregiverDetail(generics.RetrieveAPIView):
    queryset = Caregiver.objects.all()
    serializer_class = CaregiverSerializer
    permission_classes = (AllowAny,) #fixme precisa do user pra auth

class CaregiverCalendarView(generics.RetrieveAPIView):
    queryset = Caregiver.objects.all()
    serializer_class = CaregiverSerializer
    permission_classes = (AllowAny,)#fixme precisa do user pra auth
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        calendar = {
           "fixed_unavailable_days":serializer.data.get('fixed_unavailable_days', []),
           "fixed_unavailable_hours":serializer.data.get('fixed_unavailable_hours', []),
           "custom_unavailable_days":serializer.data.get('custom_unavailable_days',[])
        }

        return Response(calendar)