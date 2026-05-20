from django.db import models 
 
# Create your models here. 
class course1(models.Model): 
    coursecode = models.CharField(max_length=10) 
    coursename = models.CharField(max_length=50) 
    credits = models.IntegerField() 
 
    def __str__(self): 
        return f"{self.coursecode} - {self.coursename}"
