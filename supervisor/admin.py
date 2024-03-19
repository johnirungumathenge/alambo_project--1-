from django.contrib import admin
from .models import Approved_records, Supervisor


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = 'work','week_day','week','time','date','approved','feedback'

admin.site.register(Approved_records, MemberAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = 'fullname','email','regno','img','password'

admin.site.register(Supervisor, MemberAdmin)