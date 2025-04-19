from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Card(models.Model):
    card_number = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.card_number

class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} ({self.code})"

class Student2(models.Model):
    name = models.CharField(max_length=100)
    card = models.OneToOneField(
        Card,
        on_delete=models.PROTECT,  # Prevents card deletion if linked to student
        related_name='student'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,  # Deletes students when department is deleted
        related_name='students'
    )
    courses = models.ManyToManyField(
        Course,
        related_name='students'
    )
    
    def __str__(self):
        return self.name