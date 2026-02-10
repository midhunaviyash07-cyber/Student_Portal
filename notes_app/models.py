from django.db import models
from django.utils import timezone



class Note(models.Model):
    """
    Model to represent a note with title, content, and timestamps
    """
    title = models.CharField(max_length=200, help_text="Title of the note")
    content = models.TextField(help_text="Content of the note")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the note was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the note was last updated")

    class Meta:
        ordering = ['-updated_at']  # Show most recently updated notes first
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title

    def get_preview(self, length=100):
        """Return a preview of the content"""
        if len(self.content) > length:
            return self.content[:length] + "..."
        return self.content