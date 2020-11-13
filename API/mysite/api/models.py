from django.db import models
# from PIL import save, Image
from keras_preprocessing import image


class Bird(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Networks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    algorithm = models.CharField(max_length=50)

    def __int__(self):
        return self.id


class Results(models.Model):
    id = models.AutoField(primary_key=True)
    network_id = models.ForeignKey(Networks, on_delete=models.CASCADE)
    result = models.DecimalField(max_digits=6, decimal_places=3, default='0.000')

    def __float__(self):
        return self.result


