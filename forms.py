from django import forms
from .models import Complaint, Room, RoomDetails, Student, Admin, VisitorRequest
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields =['title','content']

class StudentRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = ['usn', 'name', 'sem', 'branch', 'ph_no', 'email', 'address', 'fathername', 'fphn_no', 'mother_name', 'password', 'confirm_password']

class StudentLoginForm(forms.Form):
    usn = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput())

# class AdminLoginForm(forms.Form):
#     admin_id = forms.CharField(max_length=10)
#     password = forms.CharField(widget=forms.PasswordInput())
# hostel/forms.py

class RoomAllocationForm(forms.ModelForm):
    class Meta:
        model = RoomDetails
        fields = ['room_no', 'usn', 'name', 'sem']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room_no'].queryset = Room.objects.filter(is_occupied=False)

class VisitorRequestForm(forms.ModelForm):
    class Meta:
        model = VisitorRequest
        fields = ['usn', 'student_name', 'visitor_name', 'relation', 'ph_no', 'visit_date', 'visit_time']



class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_text']
        widgets = {
            'complaint_text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }


# class StudentEditForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'usn', 'email', 'room', 'phone_number', 'address']  # Add other fields as necessary
