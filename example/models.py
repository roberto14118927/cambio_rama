from django.db import models

# Create your views here.

class Example2(models.Model):
    name = models.CharField(max_length=255, null=False)
    delete = models.BooleanField(default = False)
    class Meta:
        db_table = "Example2"

class Example(models.Model):
    example = models.ForeignKey(Example2, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    delete = models.BooleanField(default = False)

    class Meta:
        db_table = "Example"

