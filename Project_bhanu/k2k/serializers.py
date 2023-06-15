from rest_framework import serializers
from .models import r_lookupdata, d_user_data, r_state_district, r_k2support, r_district_data, r_farmingassets


class r_k2supportSerializer(serializers.ModelSerializer):
    class Meta:
        model = r_k2support
        fields = [ 'id', 'vedioLink', 'vedioType', 'vedioLinkHindi', 'vedioLinkLocal', 'state', 'district', 'activeInK2App', 'last_updated_at']


class r_district_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = r_district_data
        fields = ('id','village','village_hindi','gram_panchayat','tehsil','tehsil_hindi','district','district_hindi','state','state_hindi','last_updated_at')


class r_farmingassetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = r_farmingassets
        fields = ('id','seqNo','assetType','assetsubType','assetNameEnglish','assetNamehindi','assetCapacityUnit','district','state','inUse','activeInK2App','last_updated_at')

class r_lookupdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = r_lookupdata
        fields = ( 'PrimaryFunction', 'SecondaryFunction', 'PrimaryFunction_ImageName', 'SecondaryFunction_ImageName', 'canDemandSecondaryFunction',
            'isAvailableSecondaryFunction', 'areFunctionInUse', 'PrimaryFunction_hindi', 'SecondaryFunction_hindi')
class d_user_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = d_user_data
        fields = ('id', 'first_name', 'last_name', 'mobile_number', 'village', 'pincode', 'PrimaryFunction','SecondaryFunction', 'tehsil','district','last_updated_at') 
        
class r_state_districtSerializer(serializers.ModelSerializer):
    class Meta:
        model = r_state_district
        fields = ('id', 'state', 'state_hindi', 'district', 'district_hindi', 'activeInK2App','population2021','areaInKmSquare', 'densityPerKm','last_updated_at')