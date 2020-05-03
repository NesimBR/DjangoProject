import json

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm
from home.models import Setting, Contactform, ContactFormu
from note.models import Note, Category, Images, Comment


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
    comments = Comment.objects.filter(note_id=id,status='True')
    context = {'category': category, 'comments':comments, 'note': note, 'images': images}
    return render(request, 'note_detail.html', context)

def note_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                notes = Note.objects.filter(title__icontains=query)  # Select * from note where title like %query%
            else:
                notes = Note.objects.filter(title__icontains=query, Category_id=catid)   # Select * from note where title like %query%
            context = {'notes': notes,
                       'category': category,
                       'query': query
                       }
            return render(request,'note_search.html',context)
    return HttpResponseRedirect('/')


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        notes = Note.objects.filter(title__icontains=q)
        results = []
        for rs in notes:
            note_json = {}
            note_json = rs.title
            results.append(note_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)