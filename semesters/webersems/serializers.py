from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = [ 'id', 'school', 'class_num', 'credit_hours']

def get_info(self, Courses):
    dat = Courses.school
    return dat