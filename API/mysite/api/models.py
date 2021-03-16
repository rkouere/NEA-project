# Import libraries
from django.db import models


# These are all the different databases
class Bird(models.Model):
    id = models.AutoField(primary_key=True)  # Primary Key
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Network(models.Model):
    id = models.AutoField(primary_key=True)  # Primary Key
    name = models.CharField(max_length=50)

    def __int__(self):
        return self.id


class Results(models.Model):
    id = models.AutoField(primary_key=True)  # Primary Key
    network_id = models.IntegerField()  # foreign key
    result = models.BooleanField(default=False)

    def __bool__(self):
        return self.result


# Made for debugging
def test_import():
    print("Successful import")
