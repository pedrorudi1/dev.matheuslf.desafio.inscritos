from django.db import models

# Create your models here.
class Projects(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return self.name