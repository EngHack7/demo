from django.contrib import admin
from .models import Account , Grades , Videos , Subject , TeacherNotes
# Register your models here.
from django.contrib.auth.admin import UserAdmin



class AccountAdmin(UserAdmin):
	list_display = ('username', 'the_id_number',  'last_login', 'is_active' , 'is_staff')
	search_fields = ('email', 'username', 'the_id_number')
	readonly_fields = ('last_login', )

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(Videos)
admin.site.register(Grades)
admin.site.register(Subject)
admin.site.register(TeacherNotes)
