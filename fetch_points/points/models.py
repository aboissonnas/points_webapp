from django.db import models


class PointsRecord(models.Model):
    payer = models.CharField(max_length=100)
    value = models.IntegerField()
    timestamp = models.DateTimeField()
    is_spent = models.BooleanField(default=False)