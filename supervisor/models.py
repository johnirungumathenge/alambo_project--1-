from django.db import models

# Create your models here.
class Supervisor(models.Model):
    fullname = models.CharField(max_length=50)
    regno = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    img = models.ImageField(upload_to='supervisor')
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.fullname
    
class Approved_records(models.Model):
    work = models.TextField()
    week = models.CharField(max_length=30)
    week_day = models.CharField(max_length=50)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True) 
    APPROVAL_CHOICES = [
        (True, 'Approved'),
        (False, 'Not Approved'),
    ]
    approved = models.BooleanField(default=True, choices=APPROVAL_CHOICES) 
    feedback = models.TextField()
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)