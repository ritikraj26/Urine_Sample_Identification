from django.db import models
from django.core.validators import MaxValueValidator

class color(models.Model):
    red = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(limit_value=255)]
    )
    green = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(limit_value=255)]
    )
    blue = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(limit_value=255)]
    )
    
    def __str__(self):
        return f"({self.red},{self.green},{self.blue})"
    
class colors(models.Model):
    color1 = models.ForeignKey(color, on_delete=models.SET_NULL, related_name="color1", null=True, blank=True)
    color2 = models.ForeignKey(color, on_delete=models.SET_NULL, related_name="color2", null=True, blank=True)
    color3 = models.ForeignKey(color, on_delete=models.SET_NULL, related_name="color3", null=True, blank=True)
    color4 = models.ForeignKey(color, on_delete=models.SET_NULL, related_name="color4", null=True, blank=True)
    color5 = models.ForeignKey(color, on_delete=models.SET_NULL, related_name="color5", null=True, blank=True)
    color6 = models.ForeignKey(color, on_delete=models.SET_NULL, related_name="color6", null=True, blank=True)
    color7 = models.ForeignKey(color, on_delete=models.SET_NULL, related_name="color7", null=True, blank=True)
    color8 = models.ForeignKey(color, on_delete=models.SET_NULL, related_name="color8", null=True, blank=True)
    color9 = models.ForeignKey(color, on_delete=models.SET_NULL, related_name="color9", null=True, blank=True)
    color10 = models.ForeignKey(color, on_delete=models.SET_NULL, related_name="color10", null=True, blank=True)

    def __str__(self):
        return f"Colors for Urine Strip {self.id}"
  
class strip(models.Model):
    strip_image = models.ImageField(upload_to="samples/")
    strip_colors = models.ForeignKey(colors, on_delete=models.CASCADE)

    def __str__(self):
        return f"Urine Strip {self.id}"

