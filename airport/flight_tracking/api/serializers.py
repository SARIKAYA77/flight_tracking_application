from rest_framework import serializers
from .models import Airport, Flight

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['code', 'city']




class FlightSerializer(serializers.ModelSerializer):
    #to_ = serializers.RelatedField(read_only=False,queryset=Airport.objects.all())
    #from_ = serializers.RelatedField(read_only=False,queryset=Airport.objects.all())
    class Meta:
        model = Flight
        fields = "__all__"

    def to_representation(self, obj):
        return {
            "flight_number": obj.flight_number,
            "take_off": obj.take_off,
            "landing": obj.landing,
            'from':obj.from_airport.code,
            'to':obj.to_airport.code,
        }

class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        lookup_field='flight_number'
        fields = "__all__"
    
    def to_representation(self,obj):
        return {
            'flight_number':obj.flight_number,
            'count':len(Flight.objects.filter(flight_number=obj.flight_number))
        }
    
