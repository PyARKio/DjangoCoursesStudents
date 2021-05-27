from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class CourseParticipant(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.course
