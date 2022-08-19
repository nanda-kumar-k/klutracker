from rest_framework import serializers
from . import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class CodingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CodingProfile
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Certification
        fields = ['cllg_id', 'aws_cp', 'aws_da']