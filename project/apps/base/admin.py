from models import Pupil, ClassId
from django.contrib import admin


# admin.site.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    fields = ['last_name', 'first_name', 'middle_name', 'birth_date',
              'pupil_id']

admin.site.register(Pupil, PupilAdmin)


class ClassIdAdmin(admin.ModelAdmin):
    pass

admin.site.register(ClassId, ClassIdAdmin)
