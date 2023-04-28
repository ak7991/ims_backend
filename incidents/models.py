from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import random

class Incident(models.Model):
    PRIORITY = (
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW')
    )

    # Create incident id according to spec
    def create_inc_id():
        prefix = "RMG"
        five_random_nums = str(random.randint(0, 99999)).ljust(5, "0")
        current_year = str(datetime.now().year)
        target = prefix + five_random_nums + current_year
        return target
    
    incident_id = models.CharField(max_length=12, unique=True, editable=False, 
                                   default=create_inc_id, null=False)
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    description = models.TextField(max_length=128, null=True, blank=True)
    priority = models.CharField(max_length=20, null=False, choices=PRIORITY, default="LOW")
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    closed_status = models.BooleanField(null=False, default=True)

    def __str__(self):
        return f"{self.incident_id}::{self.priority}::{self.closed_status}"