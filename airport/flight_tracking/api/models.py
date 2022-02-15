from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=50)
    city = models.CharField(max_length=255)

    def __unicode__(self):
        return self.code

    def __str__(self):
        return self.code


class Flight(models.Model):
    flight_number = models.CharField(max_length=6)
    take_off = models.DateTimeField()
    landing = models.DateTimeField()
    from_airport = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="from_airport")
    to_airport = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="to_airport")

    def __str__(self):
        return self.flight_number

    @property
    def from_airport_(self):
        return self.from_airport.code

    @property
    def to_(self):
        return self.to_airport.code
