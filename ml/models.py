from django.db import models

# Create your models here.

class Tag (models.Model):
    holiday = models.IntegerField()
    week = models.IntegerField()
    time = models.IntegerField()
    gender = models.IntegerField()
    age = models.IntegerField()
    size = models.IntegerField()
    tag = models.IntegerField()

    def __str__(self):
        return "holiday:"+str(self.holiday)+"week:"+str(self.week)+"time:"+str(self.time)+"gender:"+str(self.gender)+"age:"+str(self.age)+"size:"+str(self.size)+"tag:"+str(self.tag)

