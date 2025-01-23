from django.contrib import admin
from .models import Post

# Register your models here.
from .models import agency, non_approved_agency
from .models import EmergencyReport
from .models import agency

class agencyadmin(admin.ModelAdmin):
    list_display = ('id','name', 'category_of_service','category_of_calamity')

class non_approved_agencyAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'city')
    actions = ['approve_agency']

    def approve_agency(self, request, queryset):
        for i in queryset:
            i.approve()
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content') 


class EmergencyReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'emergency_type', 'number_of_people', 'created_at')
    list_filter = ('emergency_type',)
    search_fields = ('name', 'phone_number')

admin.site.register(EmergencyReport, EmergencyReportAdmin)
admin.site.register(non_approved_agency, non_approved_agencyAdmin)
admin.site.register(agency,agencyadmin)
admin.site.register(Post, PostAdmin)