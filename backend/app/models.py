from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

        
class District(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, related_name='district', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TicketBus(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField()

    def __str__(self):
        return self.name


class Journey(models.Model):
    BUS_TYPE = [
        (1, 'Comum'),
        (2, 'Executivo'),
    ]
    
    value = models.FloatField(default=0)
    origin_region = models.ForeignKey(Region, related_name='origin_region', on_delete=models.CASCADE)
    destiny_region = models.ForeignKey(Region, related_name='destiny_region', on_delete=models.CASCADE)
    ticket_bus = models.ForeignKey(TicketBus,related_name='ticket_bus', on_delete=models.CASCADE)
    bus_type = models.CharField(
        max_length=1,
        choices=BUS_TYPE
    )

    def __str__(self):
        return self.value



