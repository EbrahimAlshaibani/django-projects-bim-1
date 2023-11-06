from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50,null=True)
    code = models.CharField( max_length=50,null=True)
    
    def __str__(self):
        return self.code


class Student(models.Model):
    name = models.CharField(max_length=50,null=True)
    last_name = models.CharField( max_length=50,null=True)
    uni_id = models.CharField( max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    name = models.CharField(max_length=50,null=True)
    last_name = models.CharField( max_length=50,null=True)
    
    def __str__(self):
        return self.name
    
