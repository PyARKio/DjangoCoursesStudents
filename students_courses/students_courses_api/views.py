from rest_framework import viewsets

from .serializers import CourseSerializer
from .serializers import StudentSerializer
from .models import Course
from .models import Student


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer
