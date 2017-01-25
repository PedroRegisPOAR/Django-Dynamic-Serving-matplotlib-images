from django.db import models

# Create your models here.


class Plot(models.Model):
	img = models.FileField()