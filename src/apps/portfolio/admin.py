from csv import list_dialects
from django.contrib import admin

from .models import Technology, Competence, Contact, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'nom_du_auteur',
        'title',
        'niveau',
        'favorites',
        'status',
        'number_views',
        'published_date',
        'update_date',
    )
    
    search_fields = (
        'title',
        'author__first_name',
        'author__last_name',
    )
    
    list_filter = (
        'niveau',
        'favorites',
        'status',
        'create_date',
        'published_date',
    )
    
    list_editable = (
        'title',
        'niveau',
        # 'technologys',
        'favorites',
        'status',
    )
    
    prepopulated_fields = {'slug': ('title',)}
    
    def nom_du_auteur(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

admin.site.register(Project, ProjectAdmin)


class TechnologyAdmin(admin.ModelAdmin):
    list_display = (
        'technology',
    )
    
    search_fields = (
        'technology',
    )
    
admin.site.register(Technology, TechnologyAdmin)


class CompetenceAdmin(admin.ModelAdmin):
    list_display = (
        'update_date',
        'sort_order',
        'title',
        'description',
        'icon',
    )
    
    search_fields = (
        'title',
    )
    
    list_editable = (
        'sort_order',
        'title',
        'description',
        'icon',
    )
    
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Competence, CompetenceAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'message',
    )
    
    search_fields = (
        'name',
        'email',
        'subject',
    )
    
admin.site.register(Contact, ContactAdmin)