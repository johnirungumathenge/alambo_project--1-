from django.contrib import admin
from .models import UpdateDetails,Student
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = 'work','week_day','Date','time','week','student'

admin.site.register(UpdateDetails, MemberAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = 'Fullname','Email','Regno','Profile','Password'

admin.site.register(Student, MemberAdmin)