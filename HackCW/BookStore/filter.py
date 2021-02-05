from django import forms
from django.contrib.auth.models import User, Group
import django_filters
from . import models



FILTER_CHOICES = [
    ('Select The University ', 'Select The University '),
]

#fetch university_book from database
universities= models.SellBook.objects.values('book_university')
#convert into list
university_list=list(universities)
# print(university_list)
#seperate key:value pair and append values to choices
for i in university_list:
    university_name=i['book_university']
    choice=(university_name,university_name)
    FILTER_CHOICES.append(choice)


class UserFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(lookup_expr='icontains')
    subject = django_filters.CharFilter(lookup_expr='icontains')
    college_name = django_filters.CharFilter(lookup_expr='icontains')
    book_university = django_filters.ChoiceFilter(lookup_expr='icontains', choices=FILTER_CHOICES)
    class Meta:
        model = User
        fields = ['book_name','subject', 'book_university','college_name']