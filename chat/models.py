from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Message(models.Model):
    msg = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    