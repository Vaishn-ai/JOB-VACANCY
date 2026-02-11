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
    salary_range = models.CharField(max_length=50, null=True)

def __str__(self):
        return self.title

from django.db import models

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
