from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','gender','Disease','doctor','doctor_fees','admit_date')