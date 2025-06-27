from rest_framework import serializers
from .models import VehicleRecord

class VehicleRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleRecord
        fields = '__all__' #includes all the fields from the model
        read_only_fields = ['total_charge']  #only reading total_charge

    def validate(self, data): #validates that exit time isnt earlier than the entry time
        entry = data.get('entry_time')
        exit_ = data.get('exit_time')

        if entry and exit_:
            if exit_ < entry:
                raise serializers.ValidationError("Exit time cannot be earlier than entry time.")
        return data
    
    #creates method to calculate the total when both entry and exit time are present
    def create(self, validated_data):
        entry = validated_data.get('entry_time')
        exit_ = validated_data.get('exit_time')

        if entry and exit_: #if i have both entries, it calculate the total_charge
            duration = exit_ - entry
            hours = duration.total_seconds() / 3600
            validated_data['total_charge'] = round(hours * 2, 2)  #base hourly rate or portion=$2.00
        else:
            validated_data['total_charge'] = None #No charge if one of the timestamps is missing 
        return super().create(validated_data)

    def update(self, instance, validated_data): #updates every field manually, and keeps values that aren't  provided
        instance.license_plate = validated_data.get('license_plate', instance.license_plate)
        instance.entry_time = validated_data.get('entry_time', instance.entry_time)
        instance.exit_time = validated_data.get('exit_time', instance.exit_time)

        # Recalculate total_charge only if both timestamps are available

        if instance.entry_time and instance.exit_time:
            duration = instance.exit_time - instance.entry_time #total duration 
            hours = duration.total_seconds() / 3600
            instance.total_charge = round(hours * 2, 2)  #the base tax for hour is $2.00 

        instance.save() #saves the updated instance to the database
        return instance

