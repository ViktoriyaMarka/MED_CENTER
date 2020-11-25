from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import *
admin.site.site_header = 'Медицинский центр'

# Register your models here.

class AccountAdmin(UserAdmin):
	list_display = ('username','surname_doctor','name_doctor','middlename_doctor','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('username', 'surname_doctor','name_doctor','middlename_doctor')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(Positions)


