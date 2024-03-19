from django.db import models

# Create your models here.
class Lecturer(models.Model):
    fullname = models.CharField(max_length=50)
    regno = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    img = models.ImageField(upload_to='lecturers')
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.fullname