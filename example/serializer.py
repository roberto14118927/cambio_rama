from rest_framework import routers, serializers

from example.models import Example
from example.models import Example2

class ExampleSerializers(serializers.ModelSerializer):
    nameExample2 = serializers.ReadOnlyField(source='example.name')
    deleteExample2 = serializers.ReadOnlyField(source='example.delete')
    class Meta:
        model = Example
        fields = ('__all__')


class Example2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fields = ('__all__')