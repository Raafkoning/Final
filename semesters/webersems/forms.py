from django import forms
from .models import *

CHOICES = (
    (1, 'YES'),
    (0, 'NO'),
)

class FormSchool(forms.ModelForm):
    fall_semester = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':"radbtns"}), choices=CHOICES)
    spring_semester = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':"radbtns"}), choices=CHOICES)
    summer_semester = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':"radbtns"}), choices=CHOICES)
    class Meta:
        model = Courses
        fields = ['school', 'class_num', 'credit_hours', 'fall_semester', 'spring_semester', 'summer_semester']

class FormSemester(forms.ModelForm):
    class1 = forms.ModelChoiceField(queryset=Courses.objects.all())
    for course in Courses.objects.all():
        if class1 == course:
            class1_ch = forms.ModelChoiceField()
    
    class2 = forms.ModelChoiceField(queryset=Courses.objects.all())
    class3 = forms.ModelChoiceField(queryset=Courses.objects.all())
    class4 = forms.ModelChoiceField(queryset=Courses.objects.all())
    class5 = forms.ModelChoiceField(queryset=Courses.objects.all())
    class Meta:
        model = Semester
        fields = ['sem_name', 'class1', 'class2', 'class3', 'class4', 'class5',]

'''
class RegCarForm(forms.ModelForm):

    dcars = {}
    list_cars = []
    for car in Car.objects.all():
        if car.brand.company_name in dcars:
            dcars[car.brand.company_name].append(car.name)
        else:
            dcars[car.brand.company_name] = [car.name]
        list_cars.append((car.name,car.name))

    brands = [str(brand) for brand in Brand.objects.all()]

    brand_select = forms.ChoiceField(choices=([(brand, brand) for brand in brands]))
    car_select = forms.ChoiceField(choices=(list_cars))

    brands = json.dumps(brands)
    cars = json.dumps(dcars)

    class Meta:
        model = Fleet
        fields = ('brand_select', 'car_select', 'description',)
'''