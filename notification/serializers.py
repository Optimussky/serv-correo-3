#from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from notification.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        #fields = '__all__' # Esto no es recomendable
        fields = ['uuid','body','email','title','created']


class NotificationSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Notification
        #fields = '__all__' # Esto no es recomendable
        fields = ['body','email','title','created']