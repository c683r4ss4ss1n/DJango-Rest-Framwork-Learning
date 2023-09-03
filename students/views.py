from django.shortcuts import render
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

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
    student = Students.objects.get(id = pk)
    serializer = StudentsSerializer(student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def students_create(request):
    if request.method == 'POST':
        json_data = request.body
        # Json to stream convert
        stream = io.BytesIO(json_data)
        #Stream to python
        pythondata = JSONParser().parse(stream)
        # Python to complex
        serializer = StudentsSerializer(data=pythondata)
        
        if serializer.is_valid():
            serializer.save()
            res = {'Message':'Successfully insert data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application.json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application.json')