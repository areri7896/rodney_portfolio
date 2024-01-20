from django.contrib import admin

from cv.models import Profile, Expertise, Project, Webinar, Education

# Register your models here.
admin.site.register(Profile)


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ('w_name',)


@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'school')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('course', 'school')
