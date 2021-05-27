from rest_framework import serializers
from .models import Course
from .models import Student


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'description', 'start_date', 'end_date')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email')
