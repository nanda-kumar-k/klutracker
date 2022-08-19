from django.db import models


class Student(models.Model):
    cllg_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    no_of_active_backlogs = models.IntegerField()
    crtchoice = models.BooleanField(default=False)
    linkdin = models.CharField(max_length=1000)
    github = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.cllg_id

class CodingProfile(models.Model):
    cllg_id = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    codechef_handle = models.CharField(max_length=100)
    codeforces_handle = models.CharField(max_length=100)
    leetcode_handle = models.CharField(max_length=100)
    vjudge_handle = models.CharField(max_length=100)
    
    def __str__(self):
        return self.cllg_id

class Certification(models.Model):
    cllg_id = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    aws_cp = models.CharField(max_length=250)
    aws_da = models.CharField(max_length=250)
    aws_sa = models.CharField(max_length=250)
    azure_900 = models.CharField(max_length=250)
    azure_240 = models.CharField(max_length=250)
    google_cloud = models.CharField(max_length=250)
    
    def __str__(self):
        return self.cllg_id

