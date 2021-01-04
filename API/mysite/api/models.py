from django.db import models


# These are all the different databases
class Bird(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Network(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # algorithm = models.CharField(max_length=50)

    def __int__(self):
        return self.id


class Results(models.Model):
    id = models.AutoField(primary_key=True)
    # network_id = models.ForeignKey(Networks, on_delete=models.CASCADE)
    network_id = models.IntegerField()  # there is no need to specify that its a foreign key as I know it is
    result = models.BooleanField(default=False)

    def __bool__(self):
        return self.result


def test_import():
    print("Successful import")
