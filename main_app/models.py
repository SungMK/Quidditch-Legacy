from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Player(models.Model):
    name=models.CharField(max_length=100)
    species=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    house=models.CharField(max_length=100)
    wizard=models.BooleanField(default=False)
    hogwarts_student=models.BooleanField(default=False)
    hogwarts_staff=models.BooleanField(default=False)
    alive=models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('players_detail', kwargs={'pk': self.id})
        
class Broomstick(models.Model):
    CHOICES = (
        ('AWG', 'Air Wave Gold'),
        ('ASF', 'Australian Flyabout'),
        ('BBTL', 'Bluebottle'),
        ('CS1', 'Cleansweep One'),
        ('CS2', 'Cleansweep Two'),
        ('CS3', 'Cleansweep Three'),
        ('CS5', 'Cleansweep Five'),
        ('CS6', 'Cleansweep Six'),
        ('CS7', 'Cleansweep Seven'),
        ('CS11', 'Cleansweep Eleven'),
        ('C140', 'Comet 140'),
        ('C180', 'Comet 180'),
        ('C220', 'Comet 220'),
        ('C260', 'Comet 260'),
        ('C290', 'Comet 290'),
        ('FBLT', 'Firebolt'),
        ('FBLTS', 'Firebolt Supreme'),
        ('MNTM', 'Moontrimmer'),
        ('N1000', 'Nimbus 1000'),
        ('N1001', 'Nimbus 1001'),
        ('N1500', 'Nimbus 1500'),
        ('N1700', 'Nimbus 1700'),
        ('N2000', 'Nimbus 2000'),
        ('N2001', 'Nimbus 2001'),
        ('OKS79', 'OAKSHAFT 79'),
        ('SS', 'Shooting Star'),
        ('SIBA', 'Siberian Arrow'),
        ('SILVA', 'Silver Arrow'),
        ('SS21', 'Starsweeper XXI'),
        ('SST', 'Swiftstick'),
        ('TB7', 'Thunderbolt VII'),
        ('TBL', 'Tinderblast'),
        ('TVB', 'Transylvanian Barb'),
        ('TB30', 'Turbo XXX'),
        ('TW90', 'Twigger 90'),
        ('VARA', 'Varápidos'),
        ('YAJI', 'Yajirushi')
    )

    choice = models.CharField(max_length=100, choices=CHOICES, default='Air Wave Gold')

    def __str__(self):
        return self.choice

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    players = models.ManyToManyField(Player)
    broomsticks = models.ManyToManyField(Broomstick)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f' Team {self.name}, {self.description}, starring: {self.players}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'team_id': self.id})