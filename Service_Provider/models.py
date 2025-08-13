from django.db import models

# Create your models here.
from django.db import models

class RemoteUserDetectionAccuracy(models.Model):
    # define your fields here, e.g.
    user_id = models.IntegerField()
    accuracy = models.FloatField()
    # add more fields as needed

    def __str__(self):
        return str(self.user_id)
