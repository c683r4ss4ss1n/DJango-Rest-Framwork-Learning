from rest_framework import serializers

class StudentsSerializer(serializers.Serializer):
    student_Name = serializers.CharField(max_length=30)
    student_Email = serializers.EmailField()
    student_Phone_Number = serializers.CharField(max_length=12)
    student_Nationality = serializers.CharField(max_length=20)
    