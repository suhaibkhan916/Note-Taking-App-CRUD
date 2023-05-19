from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes
from .forms import NoteForm


def list_all_notes(request):
    notes_obj = Notes.objects.all()
    content = {'notes': notes_obj}

    return render(request, 'notes_app/notes.html', content)


def get_note(request, pk):
    notes_obj = Notes.objects.get(table_id=pk)
    print(notes_obj)
    context = {'single_note': notes_obj}

    return render(request, 'notes_app/single-note.html',context)


def create_notes(request):
    notes_form = NoteForm()

    if request.method == 'POST':
        notes_form = NoteForm(request.POST)
        if notes_form.is_valid():
            notes_form.save()
            return redirect('notes')

    context = {'form': notes_form}
    return render(request, 'notes_app/notes_form.html', context)


def update_notes(request, pk):
    note = Notes.objects.get(table_id=pk)

    notes_form = NoteForm(instance=note)

    if request.method == 'POST':
        notes_form = NoteForm(request.POST, instance=note)
        if notes_form.is_valid():
            notes_form.save()
            return redirect('notes')

    context = {'form': notes_form}
    return render(request, 'notes_app/notes_form.html', context)


def delete_notes(request, pk):
    note = Notes.objects.get(table_id=pk)

    notes_form = NoteForm(instance=note)

    if request.method == 'POST':
        notes_form = NoteForm(request.POST, instance=note)
        if notes_form.is_valid():
            notes_form.save()
            return redirect('notes')

    context = {'form': notes_form}
    return render(request, 'notes_app/notes_form.html', context)



def delete_notes(request, pk):
    note = Notes.objects.get(table_id=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    context = {'object': note}
    return render(request, 'notes_app/delete.html', context)
