from django.shortcuts import render
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def student_info(request):
    #complex Data
    student = Students.objects.all()
    #Python Dict
    serializer = StudentsSerializer(student, many=True)
    #Render Json
    json_data = JSONRenderer().render(serializer.data)
    #Json Sent to User
    return HttpResponse(json_data, content_type='application/json')

def student_instance(request, pk):
    #complex Data
    student = Students.objects.get(id = pk)
    #Python Dict
    serializer = StudentsSerializer(student)
    #Render Json
    json_data = JSONRenderer().render(serializer.data)
    #Json Sent to User
    return HttpResponse(json_data, content_type='application/json')