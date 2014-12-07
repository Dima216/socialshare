from django.contrib import admin
from models import Join, JoinFriend

# Register your models here.
class JoinAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'ip_address', 'timestamp','updated']
	class Meta:
		model = Join
		

admin.site.register(Join, JoinAdmin)

admin.site.register(JoinFriend)