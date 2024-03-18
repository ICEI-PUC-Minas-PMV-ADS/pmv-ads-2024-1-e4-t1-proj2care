from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CareRequest, CareReceiver, Greeting, Caregiver, Rating, Specialization, Qualification
from .serializers import CareRequestSerializer, CareReceiverSerializer, GreetingSerializer, CaregiverSerializer, QualificationSerializer, RatingSerializer, SpecializationSerializer, UserSerializer

class GreetingList(APIView):
     authentication_classes =[JWTAuthentication]
     def get(self, request):
        greetings = Greeting.objects.all()
        serializer = GreetingSerializer(greetings, many=True)
        return Response(serializer.data)

class CaregiverList(generics.ListAPIView): #Não sei se essa url faz sentido já que vamos pegar do mongo, mas como não temos mongo ainda, ta ai.
    queryset = Caregiver.objects.all()  #lembrando que tem que implementar filtro tbm {query_params} quando passar pro mongo.
    serializer_class = CaregiverSerializer
    permission_classes = (AllowAny,) #fixme precisa do user pra auth
    # authentication_classes =[JWTAuthentication]

class CaregiverEdit(APIView):
    queryset = Caregiver.objects.all()
    serializer_class = CaregiverSerializer
    permission_classes = (AllowAny,) #fixme precisa do user pra auth
    authentication_classes =[JWTAuthentication]
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
    authentication_classes =[JWTAuthentication]
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
    # authentication_classes =[JWTAuthentication]
class CaregiverCalendarView(generics.RetrieveAPIView):
    queryset = Caregiver.objects.all()
    serializer_class = CaregiverSerializer
    permission_classes = (AllowAny,)#fixme precisa do user pra auth
    authentication_classes =[JWTAuthentication]
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        calendar = {
           "fixed_unavailable_days":serializer.data.get('fixed_unavailable_days', []),
           "fixed_unavailable_hours":serializer.data.get('fixed_unavailable_hours', []),
           "custom_unavailable_days":serializer.data.get('custom_unavailable_days',[])
        }

        return Response(calendar)
    
#Qualification (Odair)

class QualificationCreate(generics.CreateAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    permission_classes = (AllowAny,) #confirmar se precisa de auth 
    authentication_classes =[JWTAuthentication]
class QualificationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    permission_classes = (AllowAny,)
    authentication_classes =[JWTAuthentication]
##### Specialization - Leo #####
class SpecializationListCreateView(generics.ListCreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    authentication_classes =[JWTAuthentication]
class SpecializationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class CarereceiverDetail(generics.RetrieveAPIView):
    carereceiver = CareReceiver.objects.all()
    queryset = CareReceiver.objects.all()
    serializer_class = CareReceiverSerializer

class CarereceiverEdit(APIView):
    queryset = Caregiver.objects.all()
    serializer_class = CareReceiverSerializer
    permission_classes = (AllowAny,)

    def put(self, request, format=None):
        carereceiver = self.queryset.first() 

        serializer = CareReceiverSerializer(carereceiver, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSignup(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class CareRequestListCreate(generics.ListCreateAPIView):
    authentication_classes =[JWTAuthentication]
    queryset = CareRequest.objects.all()
    serializer_class = CareRequestSerializer

class CareRequestDetail(generics.RetrieveAPIView):
    authentication_classes =[JWTAuthentication]
    queryset = CareRequest.objects.all()
    serializer_class = CareRequestSerializer

class CareRequestAccept(APIView):
    authentication_classes =[JWTAuthentication]
    def post(self, request, pk):
        care_request = CareRequest.objects.get(pk=pk)
        care_request.status = 2 # Autorizado
        care_request.save()
        return Response({'status': 'accepted'}, status=status.HTTP_200_OK)

class CareRequestDecline(APIView):
    authentication_classes =[JWTAuthentication]
    def post(self, request, pk):
        care_request = CareRequest.objects.get(pk=pk)
        care_request.status = 1  # Recusado
        care_request.save()
        return Response({'status': 'declined'}, status=status.HTTP_200_OK)

class RatingCreate(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes =[JWTAuthentication]
class RatingDetail(generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes =[JWTAuthentication]