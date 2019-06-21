from rest_framework import routers, serializers

from example.models import Example
from example.models import Example2

class ExampleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('__all__')


class Example2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fields = ('')