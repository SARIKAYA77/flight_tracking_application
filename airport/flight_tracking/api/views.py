from rest_framework import viewsets
from .serializers import AirportSerializer, CountSerializer, FlightSerializer
from .models import Airport, Flight


class AirportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows airports to be viewed or edited.
    """
    queryset = Airport.objects.all().order_by('code')
    serializer_class = AirportSerializer


class FlightViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows flights to be viewed or edited.
    """
    queryset = Flight.objects.all().order_by('take_off')
    serializer_class = FlightSerializer


class CountViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows count flights to be viewed """
    queryset = Flight.objects.all()
    serializer_class = CountSerializer
    lookup_field = 'flight_number'
