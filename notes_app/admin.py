from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Note


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):
    """
    Admin interface for Note model
    """
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'content']
    list_per_page = 25
    summernote_fields = ('content',)
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Note Information', {
            'fields': ('title', 'content')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        """Optimize query"""
        qs = super().get_queryset(request)
        return qs.select_related()