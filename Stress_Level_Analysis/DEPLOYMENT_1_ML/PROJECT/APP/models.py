from django.db import models
from django.contrib.auth.models import User


class UserPredictModel(models.Model):


    sr = models.CharField(max_length=100)
    rr = models.CharField(max_length=100)
    t = models.CharField(max_length=100)
    lm = models.CharField(max_length=100)
    bo = models.CharField(max_length=100)
    rem = models.CharField(max_length=100)
    srh = models.CharField(max_length=100)
    hr = models.CharField(max_length=100)
    label = models.CharField(max_length=100)


def __str__(self):
    return self.sr, self.rr, self.t,self.lm,self.bo,self.rem,self.srh,self.hr,self.label