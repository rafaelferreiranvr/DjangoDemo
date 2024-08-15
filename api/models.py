from django.db import models

class Data(models.Model):
    boolean_field = models.fields.BooleanField(default=False)
    text_field = models.fields.TextField(default="")
    int_field = models.fields.IntegerField(default=0)
    float_field = models.fields.FloatField(default=0)

    def update(self, data):
        self.boolean_field = data['boolean_field']
        self.text_field = data['text_field']
        self.int_field = data['int_field']
        self.float_field = data['float_field']
        self.save()
        