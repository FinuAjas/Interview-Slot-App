from django.db import models

class Availability(models.Model):
    ROLE = [
        ('Candidate', 'Candidate'), 
        ('Interviewer', 'Interviewer')
    ]

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.BigIntegerField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} {self.role}"