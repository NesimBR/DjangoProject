from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, Contactform, ContactFormu
from note.models import Note, Category, Images


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Note.objects.all()[:4]
    category = Category.objects.all()
    dayNotes = Note.objects.all()[:5]
    lastNotes = Note.objects.all().order_by('-id')[:5]
    randomNote = Note.objects.all().order_by('?')[:4]
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'dayNotes': dayNotes,
               'sliderdata': sliderdata,
               'lastNotes': lastNotes,
               'randomNote': randomNote}
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category}
    return render(request, 'aboutus.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category}
    return render(request, 'references.html', context)


def contactus(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = Contactform()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent. Thank you!")
            return HttpResponseRedirect('/contactus')
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    category = Category.objects.all()
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'contactus.html', context)


def category_notes(request, id, slug):
    notes = Note.objects.filter(Category_id=id)
    category = Category.objects.all()
    categorydata=Category.objects.get(pk=id)
    context = {'notes': notes, 'category': category, 'categorydata':categorydata}
    return render(request, 'notes.html', context)


def note_detail(request, id, slug):
    category = Category.objects.all()
    note = Note.objects.get(pk=id)
    images = Images.objects.filter(note_id=id)
    context = {'category': category, 'note': note, 'images': images}
    return render(request, 'note_detail.html',context)
