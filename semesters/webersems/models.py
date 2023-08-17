from django.db import models

class Link(models.Model):

    def __str__(self):
        return self.name
    
    address = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=1000, null=True)

SCHOOL_CHOICES = (
    ('MATH', 'MATH'),
    ('CS', 'CS'),
    ('ENGL', 'ENGL'),
    ('ETC', 'ETC'),
    ('COMM', 'COMM'),
    ('LIBS', 'LIBS'),
    ('BTNY', 'BTNY'),
    ('CHEM', 'CHEM'),    
)

CHOICES = (
    (1, 'YES'),
    (0, 'NO'),
)

HOUR_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class Courses(models.Model):
    school = models.CharField(max_length=4, choices=SCHOOL_CHOICES, default='CS')
    class_num = models.CharField(max_length=4)
    credit_hours = models.IntegerField(choices=HOUR_CHOICES, default=4)
    fall_semester = models.IntegerField(choices=CHOICES, default=1)
    spring_semester = models.IntegerField(choices=CHOICES, default=1)
    summer_semester = models.IntegerField(choices=CHOICES, default=1)
    prereq = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('school','class_num')


    def __str__(self):
        return (self.school+self.class_num)
    
class Semester(Courses):
    sem_name = models.CharField(max_length=50)
    class1 = models.CharField(max_length=8, null=True, blank=True)
    class2 = models.CharField(max_length=8, null=True, blank=True)
    class3 = models.CharField(max_length=8, null=True, blank=True)
    class4 = models.CharField(max_length=8, null=True, blank=True)
    class5 = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return (self.sem_name)
    
