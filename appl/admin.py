from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
from .forms import *

#
# class CustomizedAdmin(UserAdmin):
#     add_form = SimpleUserForm
#     form = SimpleUserChangeForm
#     model = SimpleUser
#     list_display = ['email', 'username', 'userImg']
#
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('userImg',)}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('userImg',)}),
#     )


admin.site.register(Article)
admin.site.register(Appointment)
admin.site.register(Customer)
admin.site.register(Master)
admin.site.register(Service)
admin.site.register(Editor)
# admin.site.register(SimpleUser,CustomizedAdmin)
#
