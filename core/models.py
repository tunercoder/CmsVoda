# from django.db import models
from django.db import models

class Human(models.Model):
    
    msisdn = models.BigIntegerField()
    requestdatetime = models.DateTimeField()
    smstext = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.msisdn} {self.requestdatetime} {self.smstext}'
