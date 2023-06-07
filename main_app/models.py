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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})
    
class Broomstick(models.Model):
    CHOICES = [
        ('Air Wave Gold'),
        ('Australian Flyabout'),
        ('Bluebottle'),
        ('Cleansweep One'),
        ('Cleansweep Two'),
        ('Cleansweep Three'),
        ('Cleansweep Five'),
        ('Cleansweep Six'),
        ('Cleansweep Seven'),
        ('Cleansweep Eleven'),
        ('Comet 140'),
        ('Comet 180'),
        ('Comet 220'),
        ('Comet 260'),
        ('Comet 290'),
        ('Firebolt'),
        ('Firebolt Supreme'),
        ('Moontrimmer'),
        ('Nimbus 1000'),
        ('Nimbus 1001'),
        ('Nimbus 1500'),
        ('Nimbus 1700'),
        ('Nimbus 2000'),
        ('Nimbus 2001'),
        ('OAKSHAFT 79'),
        ('Shooting Star'),
        ('Siberian Arrow'),
        ('Silver Arrow'),
        ('Starsweeper XXI'),
        ('Swiftstick'),
        ('Thunderbolt VII'),
        ('Tinderblast'),
        ('Transylvanian Barb'),
        ('Turbo XXX'),
        ('Twigger 90'),
        ('Varápidos'),
        ('Yajirushi')
    ]

    choice = models.CharField(max_length=100, choices=CHOICES, default='Air Wave Gold')

    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice

