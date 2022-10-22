from tokenize import Name
from rest_framework import serializers
from .models import ChildData, MaleUserData, Marriage, FemaleUserData, ChildData, Tender, Vacancy

class MaleUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaleUserData
        # fields = '__all__'
        exclude = ('status',)

class FemaleUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FemaleUserData
        # fields = '__all__'
        exclude = ('status',)

class CreateCIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildData
        fields = '__all__'


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Register
#         fields = '__all__'

class MarriageSerializer(serializers.ModelSerializer):
    ##Your Detail
    CID = serializers.ReadOnlyField(source='YOUR_CId.CID')
    Name = serializers.ReadOnlyField(source='YOUR_CId.Name')
    Gender = serializers.ReadOnlyField(source='YOUR_CId.Gender')
    village = serializers.ReadOnlyField(source='YOUR_CId.Village')
    chiwog = serializers.ReadOnlyField(source='YOUR_CId.Chiwog')
    contact = serializers.ReadOnlyField(source='YOUR_CId.contact_number')
    Email = serializers.ReadOnlyField(source='YOUR_CId.email')

    Spouse_name = serializers.ReadOnlyField(source='Spouce_ID.Name')
    Spouse_gender = serializers.ReadOnlyField(source='Spouce_ID.Gender')
    female = FemaleUserDataSerializer

    #

    class Meta:
        model = Marriage
        # fields = '_'
        exclude = ('status',)

    


class ChildDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildData
        fields = '__all__'

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = '__all__'
    
class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'