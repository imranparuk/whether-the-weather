from django.db import models

# date, min temp, max temp, wind speed, rain probability
# qwe123456

class Forecasts(models.Model):
    class Meta:
        verbose_name_plural = "Forecasts"
        ordering = ['-date']
        
    date = models.DateTimeField()
    min_temp = models.IntegerField()
    max_temp = models.IntegerField()
    wind_speed = models.IntegerField()
    rain_probability = models.IntegerField()
