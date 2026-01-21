from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100, null=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    description = models.TextField()
    posted_date = models.DateTimeField()   
    application_deadline = models.DateTimeField()

def __str__(self):
        return self.title