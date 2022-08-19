from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models
import json
# https://www.youtube.com/watch?v=TmsD8QExZ84


# @api_view(['GET'])
# def Home (request):
#      return Response({"message": "Hello World"})

@api_view(['GET'])
def Home (request):
     stu = models.Student.objects.all()
     serializer = serializers.StudentSerializer(stu, many=True)
     return Response(serializer.data)

@api_view(['POST'])
def SaveStudent (request):
     stu = serializers.StudentSerializer(data=request.data)
     # print(stu.validated_data)
     # if stu.is_valid():
     #      print(stu.validated_data)
     print("ttttttttttttttttttttttttttttttttttttttttttttttttttttt")
     print(request.data['cllg_id'])
     print(stu)
     if stu.is_valid(raise_exception=True):
               stu.save()
     return Response(stu.data)

@api_view(['POST'])
def StuUpdate (request, pk):
     stu = models.Student.objects.get(pk=pk)
     serializer = serializers.StudentSerializer(instance=stu, data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data)


@api_view(['POST'])
def UpdateStudent(request):
     total_data = request.data
     Stu_data = {
          'cllg_id': total_data['cllg_id'],
          'name': total_data['name'],
          'email': total_data['email'],
          'department': total_data['department'],
          'cgpa': total_data['cgpa'],
          'no_of_active_backlogs': total_data['no_of_active_backlogs'],
          'crtchoice': total_data['crtchoice'],
          'linkdin': total_data['linkdin'],
          'github': total_data['github']
     }
     stu = serializers.StudentSerializer(data=Stu_data)
     if stu.is_valid(raise_exception=True):
          stu.save()
          coding_data = {
               'cllg_id': total_data['cllg_id'],
               'codechef_handle': total_data['codechef_handle'],
               'codeforces_handle': total_data['codeforces_handle'],
               'leetcode_handle': total_data['leetcode_handle'],
               'vjudge_handle': total_data['vjudge_handle']
          }
          cd_serializer = serializers.CodingProfileSerializer(data=coding_data)
          if cd_serializer.is_valid(raise_exception=True):
               cd_serializer.save()
               cert_data = {
                    'cllg_id': total_data['cllg_id'],
                    'aws_cp': total_data['aws_cp'],
                    'aws_da': total_data['aws_da'],
                    # 'aws_sa': total_data['aws_sa'],
                    # 'azure_900': total_data['azure_900'],
                    # 'azure_240': total_data['azure_240'],
                    # 'google_cloud': total_data['google_cloud']
               }
               cert_serializer = serializers.CertificationSerializer(data=cert_data)
               if cert_serializer.is_valid(raise_exception=True):
                    cert_serializer.save()
          
     return Response("Success")


