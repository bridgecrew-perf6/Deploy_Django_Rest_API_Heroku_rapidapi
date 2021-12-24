from rest_framework.serializers import ModelSerializer
from .models import WFMTTaskModel

class WFMTMSerializer(ModelSerializer):
    class Meta:
        model=WFMTTaskModel
        fields="__all__"