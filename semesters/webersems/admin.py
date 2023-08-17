from django.contrib import admin
from .models import Link, Courses, Semester 

admin.site.register(Link)
#admin.site.register(CollegeMajor)
admin.site.register(Courses)
admin.site.register(Semester)

