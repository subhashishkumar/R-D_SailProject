from django.contrib import admin
from inputforms.models import *

# Register your models here.
class AllAccidentTable(admin.ModelAdmin):
    list_display = (
        'unit_name', 'emp_id', 'emp_type', 'emp_name', 'age', 'dept', 'shift',
        'accd_type', 'date', 'cause', 'narrative', 'learning_point',
    )


class ManhoursTable(admin.ModelAdmin):
    list_display = (
        'unit_name', 'date', 'manhours_worked_regular', 'manhours_worked_contract', 'mandays_lost',
        'RLTIFR', 'LTIFR', 'SEVERITY_RATE',
    )


admin.site.register(AllAccident, AllAccidentTable)
admin.site.register(Manhours, ManhoursTable)