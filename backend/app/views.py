from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, authentication, status
from rest_framework.views import APIView
from app.serializers import DistrictSerializer, RegionSerializer, TicketBusSerializer, JourneySerializer
from app.models import Region, District, TicketBus, Journey
from rest_framework.response import Response


class DistrictViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegionViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TicketBusViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = TicketBus.objects.all()
    serializer_class = TicketBusSerializer
    permission_classes = [permissions.IsAuthenticated]


class JourneyView(APIView):
    pagination_class = None
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # 1 centro, 2 continente, 3norte, 4 sul 5 leste
    def calculate_new_value(self, bus_type, origin_region, destiny_region):
        price = (4 if bus_type is 1 else 7)
        additional = 0.60
        if origin_region != destiny_region:
            if origin_region == 1:
                price = price + additional
            elif origin_region == 2 and destiny_region !=  1:
                price = price + (additional * 2)
            elif origin_region == 3  and destiny_region !=  1 and destiny_region !=  5:
                price = price + (additional * 2)
            elif origin_region == 4  and destiny_region !=  1 and destiny_region !=  5:
                price = price + (additional * 2)
            elif origin_region == 5 and destiny_region == 2:
                price = price + (additional * 2)
            else:
                price = price + additional
        return price

    def get(self, request, format=None):
        result = Journey.objects.all()
        serializer = JourneySerializer(result, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        data = request.data.copy().get('data')
        ticket = TicketBus.objects.get(pk=int(data['ticket_bus']))
        price = self.calculate_new_value(int(data['bus_type']), int(data['origin_region']), int(data['destiny_region']))
        if ticket.value >=  price: 
            data['value'] = price
            serializer = JourneySerializer(data=data)
            ticket.value = ticket.value - price
            if serializer.is_valid():
                serializer.save()
                ticket.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Don't have enough Credits", status=status.HTTP_400_BAD_REQUEST)

    


