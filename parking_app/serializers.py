from rest_framework import serializers
from .models import VehicleRecord

class VehicleRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleRecord
        fields = '__all__'
        read_only_fields = ['total_charge']  

    def validate(self, data):
        entry = data.get('entry_time')
        exit_ = data.get('exit_time')

        if entry and exit_:
            if exit_ < entry:
                raise serializers.ValidationError("Exit time cannot be earlier than entry time.")
        return data

    def create(self, validated_data):
        entry = validated_data.get('entry_time')
        exit_ = validated_data.get('exit_time')

        if entry and exit_:
            duration = exit_ - entry
            hours = duration.total_seconds() / 3600
            validated_data['total_charge'] = round(hours * 2, 2)  
        else:
            validated_data['total_charge'] = None

        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.license_plate = validated_data.get('license_plate', instance.license_plate)
        instance.entry_time = validated_data.get('entry_time', instance.entry_time)
        instance.exit_time = validated_data.get('exit_time', instance.exit_time)

        if instance.entry_time and instance.exit_time:
            duration = instance.exit_time - instance.entry_time
            hours = duration.total_seconds() / 3600
            instance.total_charge = round(hours * 2, 2)  

        instance.save()
        return instance
