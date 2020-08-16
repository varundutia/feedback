from django.db import models

# Create your models here.
class Fb(models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    feed = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
class Meta:
    db_table = 'feedback'