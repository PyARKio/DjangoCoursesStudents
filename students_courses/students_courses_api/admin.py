from django.contrib import admin
from .models import Course
from .models import Student
from .models import CourseParticipant

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(CourseParticipant)
