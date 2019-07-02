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
    img = models.ImageField(upload_to='media/', null=True)
    delete = models.BooleanField(default = False)

    class Meta:
        db_table = "Example"

# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, null=False)
#     delete = models.BooleanField(default = False)

#     class Meta:
#         db_table = "Example"


#         c28185bb764fad558376bdb8b7fda1807153fae2

