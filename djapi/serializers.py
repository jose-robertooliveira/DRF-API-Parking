from djapi.models import Parking
from rest_framework import serializers


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ['id', 'plate_number', 'time', 'paid', 'left']
   

    def validate(self, data):
        if data['paid'] == False:
            raise serializers.ValidationError({"paid": "Forbidden to leave without paying parking"})
        return data
        