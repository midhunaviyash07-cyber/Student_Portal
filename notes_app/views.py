from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    Display all notes
    """
    notes = Note.objects.all()
    context = {
        'notes': notes,
        'total_notes': notes.count()
    }
    return render(request, 'notes_app/note_list.html', context)


def note_create(request):
    """
    Create a new note
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            messages.success(request, f'Note "{note.title}" created successfully!')
            return redirect('note_list')
    else:
        form = NoteForm()
    
    context = {
        'form': form,
        'title': 'Create New Note',
        'button_text': 'Create Note'
    }
    return render(request, 'notes_app/note_form.html', context)


def note_edit(request, pk):
    """
    Edit an existing note
    """
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            messages.success(request, f'Note "{note.title}" updated successfully!')
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    
    context = {
        'form': form,
        'note': note,
        'title': 'Edit Note',
        'button_text': 'Update Note'
    }
    return render(request, 'notes_app/note_form.html', context)


def note_delete(request, pk):
    """
    Delete a note
    """
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == 'POST':
        note_title = note.title
        note.delete()
        messages.success(request, f'Note "{note_title}" deleted successfully!')
        return redirect('note_list')
    
    context = {
        'note': note
    }
    return render(request, 'notes_app/note_confirm_delete.html', context)


def note_detail(request, pk):
    """
    View a single note in detail
    """
    note = get_object_or_404(Note, pk=pk)
    context = {
        'note': note
    }
    return render(request, 'notes_app/note_detail.html', context)