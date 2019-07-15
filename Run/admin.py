from django.contrib import admin
from . models import Profile,Conferences,Webinars,Collab,Certify,Industry,Research1,Research2
# Register your models here.


"""class Profileadmin(admin.ModelAdmin):
    list_display=('conferences__activity',)
    search_field=['user.username','conferences__activity',]
"""

"""from django.contrib.admin.views.main import ChangeList
from Run.forms import ProfileChangeListForm
"""
"""class ProfileChangeList(ChangeList):

    def __init__(self, request, model, list_display,
        list_display_links, list_filter, date_hierarchy,
        search_fields, list_select_related, list_per_page,
        list_max_show_all, list_editable, model_admin):

        super(ProfileChangeList, self).__init__(request, model,
            list_display, list_display_links, list_filter,
            date_hierarchy, search_fields, list_select_related,
            list_per_page, list_max_show_all, list_editable,
            model_admin)

        # these need to be defined here, and not in MovieAdmin
        self.list_display = ['action_checkbox', 'user.username', 'conferences']
        self.list_display_links = ['user.username']
        self.list_editable = ['conferences']

class ProfileAdmin(admin.ModelAdmin):

    def get_changelist(self, request, **kwargs):
        return ProfileChangeList

    def get_changelist_form(self, request, **kwargs):
        return ProfileChangeListForm"""

class ConferencesAdmin(admin.ModelAdmin):
    list_display=('profile1','activity',)
    list_filter=('profile1','activity',)

class WebinarsAdmin(admin.ModelAdmin):
    list_display=('profile1','activity',)
    list_filter=('profile1','activity',)

class CollabAdmin(admin.ModelAdmin):
    list_display=('profile1','activity',)
    list_filter=('profile1','activity',)

class CertifyAdmin(admin.ModelAdmin):
    list_display=('profile1','activity',)
    list_filter=('profile1','activity',)

class IndustryAdmin(admin.ModelAdmin):
    list_display=('profile1','activity',)
    list_filter=('profile1','activity',)

class Research1Admin(admin.ModelAdmin):
    list_display=('profile1','title',)
    list_filter=('profile1','title',)

class Research2Admin(admin.ModelAdmin):
    list_display=('profile1','title',)
    list_filter=('profile1','title',)


admin.site.register(Profile)
admin.site.register(Conferences,ConferencesAdmin)
admin.site.register(Webinars,WebinarsAdmin)
admin.site.register(Collab,CollabAdmin)
admin.site.register(Certify,CertifyAdmin)
admin.site.register(Industry,IndustryAdmin)
admin.site.register(Research1,Research1Admin)
admin.site.register(Research2,Research2Admin)
