from django.db import models

class users(models.Model):
    uid = models.CharField(max_length=50, null=False)
    created_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.uid

class booking(models.Model):
    bid = models.CharField(max_length=50, default='0', null=False)
    roomtype = models.CharField(max_length=20, null=False)
    roomamount = models.CharField(max_length=5, null=False)
    datein = models.CharField(max_length=20, null=False)
    dateout = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return self.id
