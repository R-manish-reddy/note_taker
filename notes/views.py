from django.shortcuts import render,redirect
from .models import Note
from .forms import NoteForm
from datetime import date
# Create your views here.
today = date.today()
d1 = today.strftime("%d/%m/%Y")
def note_list(request):
    notes = Note.objects.all() #returns all entries in note model
    
    
    context = {
        "notes": notes,
        "date" : d1
    }
    return render(request,"notes.html",context)

def note_retrieve(request,pk):
    note = Note.objects.get(id=pk)
    context ={
        "note": note,
        "date" : d1
    }
    return render(request,"note.html",context)

def create_note(request):
    form= NoteForm()
    
    if request.method =="POST":
        form = NoteForm(request.POST)
        print(request.POST)
        if form.is_valid:
            #todo
            form.save()
            return redirect("/")
    context={
        "form": form
    }
    return render(request,"note_create.html",context)

def delete_note(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return redirect('/')

def update_note(request,pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)
    if request.method=="POST" :
        form= NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form" : form
    }
    return render(request,"note_update.html",context)