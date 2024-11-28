from rest_framework import serializers
from .models import Availability

class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = ['user_id', 'email', 'phone_number', 'role', 'start_time', 'end_time']
        read_only_fields = ['user_id']

    def validate_phone_number(self, value):
        if len(str(value)) != 10:
            raise serializers.ValidationError("Phone number should be exactly 10 digits.")
        return value