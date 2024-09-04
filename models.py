from django.db import models
from django.contrib.auth.models import User
# hostel/models.py

    
class Room(models.Model):
    room_no = models.IntegerField(unique=True)
    no_of_beds = models.IntegerField()
    is_occupied = models.BooleanField(default=False)  # New field

    def __str__(self):
        return f"Room{self.room_no}"


class Student(models.Model):
    usn = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    sem = models.IntegerField()
    branch = models.CharField(max_length=100)
    ph_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    fathername = models.CharField(max_length=100)
    fphn_no = models.IntegerField()
    mother_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.usn

class Admin(models.Model):
    admin_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)

class RoomDetails(models.Model):
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sem = models.IntegerField()

    def __str__(self):
        return f"{self.name} - Room{self.room_no}"



class VisitorRequest(models.Model):
    usn = models.CharField(max_length=10)
    student_name = models.CharField(max_length=100)
    visitor_name = models.CharField(max_length=100)
    relation = models.CharField(max_length=50)
    ph_no = models.CharField(max_length=15)
    visit_date = models.DateField()
    visit_time = models.TimeField()
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title 
    

class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    complaint_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.usn} - {self.complaint_text[:20]}"
