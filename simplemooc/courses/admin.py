from django.contrib import admin

from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug', 'start_date', 'created_at']
	search_fields = ['name', 'slug']
	#popula o campo 'Slug' de acordo com o digitado no campo 'Nome'
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)