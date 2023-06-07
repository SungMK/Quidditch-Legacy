from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Player(models.Model):
    name=models.CharField(max_length=100)
    species=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    house=models.CharField(max_length=100)
    wizard=models.BooleanField()
    hogwarts_student=models.BooleanField()
    hogwarts_staff=models.BooleanField()
    alive=models.BooleanField()
    image=models.URLField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    broomsticks = models.ManyToManyField(Broomstick)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})
    


