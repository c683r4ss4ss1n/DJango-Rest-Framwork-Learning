from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Contact
from rest_framework.views import APIView

def homeView(request):
    return render(request, 'index.html')



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def firstAPI(request):
    if request.method == 'POST':
        name = request.data['name']
        age = request.data['age']
        print(name, age)
        return Response({'name': name, 'age':age})
    
    context={
        'name' : 'Eshan',
        'University' : 'DIU'
    }
    return Response(context)



@api_view(['POST'])
def registrationAPI(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']

        if User.objects.filter(username = username).exists():
            return Response({'error': 'An user with this username already exists!'})
        if password1 != password2:
            return Response({'error':'password didnot match'})
        
        user = User()
        user.username =username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True

        user.set_password(raw_password = password1)
        user.save()

        return Response({'Success' : 'User successfully registered'})
    

# def Contact(request):
#     if request.method == 'POST':
#         data = request.data

#         name = data['name']
#         email = data['email']
#         subject = data['subject']
#         phone = data['phone']
#         details = data['details']

#         contact = Contact(name=name, email=email,subject=subject, phone=phone, details=details)
#         contact.save()

#         return Response({'Success':'Successfully saved'})
    
class ContactAPIView(APIView):
    permission_classes=[AllowAny,]
    def post(self, request, format=None):
        data = request.data

        name = data['name']
        email = data['email']
        subject = data['subject']
        phone = data['phone']
        details = data['details']

        contact = Contact(name=name, email=email,subject=subject, phone=phone, details=details)
        contact.save()
        return Response({'Success':'Succesfully Saved'})
    
    def get(self, request, format=None):
            return Response({'Success':'Succesfully Saved From Get'})
