from django.db import models


class product(models.Model):
    ean = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=70, null=False)
    fullname = models.CharField(max_length=70, null=False)
    price = models.FloatField(null=False)
    photo = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.name


class store(models.Model):
    name = models.CharField(max_length=70, null=False)
    phone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


class location(models.Model):
    zip_code = models.CharField(max_length=9, null=False)
    address = models.CharField(max_length=70, null=False)
    address_number = models.CharField(max_length=10, null=False)
    neighborhood = models.CharField(max_length=50, null=False)
    complement = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.city
