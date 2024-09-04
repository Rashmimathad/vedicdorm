# hostel/views.py

from ssl import AlertDescription
from django.shortcuts import  render, redirect
from .forms import  StudentRegistrationForm, StudentLoginForm, RoomAllocationForm, VisitorRequestForm,AnnouncementForm,ComplaintForm
from .models import Student, Room, RoomDetails, VisitorRequest,Announcement
# from .forms import AdminLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')


def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                form.save()
                return redirect('student_login')
            else:
                form.add_error('confirm_password', "Passwords do not match")
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_register.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            usn = form.cleaned_data['usn']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(usn=usn, password=password)
                request.session['usn'] = student.usn  # Store usn in session
                return redirect('student_home')
            except Student.DoesNotExist:
                messages.error(request, "Invalid USN or password")
    else:
        form = StudentLoginForm()
    return render(request, 'student_login.html', {'form': form})

# def admin_login(request):
#     if request.method == 'POST':
#         form = AdminLoginForm(request.POST)
#         if form.is_valid():
#             admin_id = form.cleaned_data['admin_id']
#             password = form.cleaned_data['password']
#             try:
#                 admin = Admin.objects.get(admin_id=admin_id, password=password)
#                 return redirect('admin_home')
#             except Admin.DoesNotExist:
#                 messages.error(request, "Invalid Admin ID or password")
#         else:
#             messages.error(request, form.errors)  # This will collect and display all errors
#     else:
#         form = AdminLoginForm()
    
#     return render(request, 'admin_login.html', {'form': form})  

def admin_home(request):
    return render(request, 'admin_home.html')

def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Redirect to admin home or announcements list
    else:
        form = AnnouncementForm()
    return render(request, 'create_announcement.html',{'form':form})

# def student_home(request):
#     usn = request.session.get('usn')
#     if not usn:
#         return redirect('student_login')
#     room_details = RoomDetails.objects.filter(usn__usn=usn)
#     announcements = Announcement.objects.all().order_by('-created_at')
#     return render(request, 'student_home.html', {'room_details': room_details, 'announcements':announcements})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def room_details(request):
    rooms = Room.objects.all()
    room_details = RoomDetails.objects.all()
    return render(request, 'room_details.html', {'rooms': rooms, 'room_details': room_details})



def allocate_room(request):
    if request.method == 'POST':
        form = RoomAllocationForm(request.POST)
        if form.is_valid():
            room_no = form.cleaned_data['room_no']
            usn = form.cleaned_data['usn']
            semester = form.cleaned_data['sem']

            room = Room.objects.get(room_no=room_no)
            student = Student.objects.get(usn=usn)

            room_detail = RoomDetails().allocate_room(room, student, semester)

            return redirect('admin_home')
    else:
        form = RoomAllocationForm()
    return render(request, 'allocate_room.html', {'form': form})


def visitor_request(request):
    if request.method == 'POST':
        form = VisitorRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitor_request_success')
    else:
        form = VisitorRequestForm()
    return render(request, 'visitor_request.html', {'form': form})

def visitor_request_success(request):
    return render(request, 'visitor_request_success.html')


def visitor_request_status(request, usn):
    requests = VisitorRequest.objects.filter(usn=usn)
    return render(request, 'visitor_request_status.html', {'requests': requests})


@login_required
def student_home(request):
    usn = request.session.get('usn')
    if not usn:
        return redirect('student_login')
    room_details = RoomDetails.objects.filter(usn__usn=usn)
    announcements = Announcement.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.student =Student.objects.get(usn=usn) # type: ignore
            complaint.save()
            messages.success(request, 'Complaint submitted successfully!')
            return redirect('student_home')
    else:
        form = ComplaintForm()

    return render(request, 'student_home.html', {'room_details': room_details, 'announcements':announcements,'form': form})

# @login_required
# def edit_student(request, pk):
#     student = get_object_or_404(Student, pk=pk)

#     if request.method == 'POST':
#         form = StudentEditForm(request.POST,instance=student)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Student details updated successfully!')
#             return redirect('admin:app_student_changelist')  # Redirect to the student list in the admin
#     else:
#         form = StudentEditForm(instance=student)

#     return render(request, 'edit_student.html',{'form': form, 'student':student})