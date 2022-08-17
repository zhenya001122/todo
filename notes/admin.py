from django.contrib import admin

from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "text", "created_at")
    list_filter = ("created_at",)
    fields = ("author", "title", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "text")
    raw_id_fields = ("author",)