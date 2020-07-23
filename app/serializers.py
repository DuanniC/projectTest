from rest_framework import serializers
from .models import *

class ProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ('ean', 'name','fullname', 'price', 'photo')

