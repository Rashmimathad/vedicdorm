from traceback import format_tb
from django.contrib import admin
from django.urls import path
from .models import Complaint, Student, Room, RoomDetails, Admin, VisitorRequest,Announcement

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('usn', 'name', 'sem', 'branch', 'ph_no', 'email', 'address', 'fathername', 'fphn_no', 'mother_name')
  
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'no_of_beds', 'is_occupied')
    

@admin.register(RoomDetails)
class RoomDetailsAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'usn', 'name', 'sem')
    


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin_id',)

# @admin.register(allocate_room)
# class AllocateRoom(admin.ModelAdmin):
#     list_display = ('room_no', 'usn', 'name', 'sem')
#     actions = ['allocate_rooms']

#     def allocate_rooms(self, request, queryset):
#         for room_detail in queryset:
#             room = room_detail.room_no
#             room.is_occupied = True
#             room.save()
#             room_detail.save()
#         self.message_user(request, "Rooms allocated successfully.")

#     allocate_rooms.short_description = "Allocate  rooms to students"

@admin.register(VisitorRequest)
class VisitorRequestAdmin(admin.ModelAdmin):
    list_display = ('usn', 'student_name', 'visitor_name', 'relation', 'ph_no', 'visit_date', 'visit_time', 'request_date', 'status')
    search_fields = ('usn', 'student_name', 'visitor_name', 'visit_date')
    list_filter = ('status', 'visit_date')
    
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display =('title','content','created_at')


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('student', 'complaint_text', 'created_at')
    search_fields = ('student__usn', 'complaint_text')
    list_filter = ('created_at',)

admin.site.register(Complaint, ComplaintAdmin)

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'usn', 'email', 'room', 'phone_number', 'address', 'edit_link']

#     def edit_link(self, obj):
#         return format_tb('<a href="{}">Edit</a>', f'/edit-student/{obj.pk}/')
#     edit_link.short_description = 'Edit'

#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('edit-student/<int:pk>/', self.admin_site.admin_view(edit_student), name='edit-student'),
#         ]
#         return custom_urls + urls

# admin.site.register(Student,StudentAdmin)