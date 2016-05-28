from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.CharField(max_length=9, primary_key=True)
    sais_number = models.CharField(max_length=8, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    current_address = models.OneToOneField('Address', related_name='+')
    home_address = models.OneToOneField('Address', related_name='+')
    birthday = models.DateField()
    program_id = models.ForeignKey('Program', related_name='students')
    mother_name = models.CharField(max_length=50)
    mother_contact = models.CharField(max_length=20)
    father_name = models.CharField(max_length=50)
    father_contact = models.CharField(max_length=20)
    year_begin = models.DateField()
    institution_id = models.ForeignKey('Institution', related_name='students')


class Program(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)


class Address(models.Model):
    street = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)


class Course(models.Model):
    CATEGORY_CHOICES = (
        ('MST', 'Math, Science, and Technology'),
        ('SSP', 'Social Sciences and '),
        ('AH', 'Arts and Humanities'),
    )
    name = models.CharField(max_length=20)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    schedule = models.CharField(max_length=20)
    instructor_id = models.ForeignKey(
        'Instructor', related_name='courses_handled')
    units = models.IntegerField(default='2')
    room = models.CharField(max_length=20)


class Instructor(models.Model):
    name = models.CharField(max_length=50)


class Institution(models.Model):
    name = models.CharField(max_length=50)
