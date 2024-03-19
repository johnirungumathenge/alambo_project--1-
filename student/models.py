from django.db import models

# Create your models here.
class Student(models.Model):
    Fullname = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Regno = models.CharField(max_length=30)
    Profile = models.ImageField(upload_to='students', null=False, blank=True)
    Password = models.CharField(max_length=255)

    def __str__(self):
        return self.Fullname

# update details
class UpdateDetails(models.Model):
    WEEK_CHOICES = models.TextChoices('WeekChoices', 'Week1 Week2 Week3 Week4 Week5 Week6 Week7 Week8 Week9 Week10')
    DAY_CHOICES = (
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
   )
    work = models.TextField()
    week= week = models.CharField(max_length=50, choices=WEEK_CHOICES.choices) 
    week_day = models.CharField(max_length=30, choices=DAY_CHOICES, default='Monday')
    Date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True)    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.work

 
