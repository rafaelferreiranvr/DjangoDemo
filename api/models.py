from django.db import models

class Data(models.Model):
    boolean_field = models.fields.BooleanField(default=False)
    text_field = models.fields.TextField(default="")
    int_field = models.fields.IntegerField(default=0)
    float_field = models.fields.FloatField(default=0)