import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, Contactform, ContactFormu, FAQ, UserProfile
from note.models import Note, Category, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Note.objects.filter(status='True')[:4]
    category = Category.objects.all()
    dayNotes = Note.objects.filter(status='True')[:10]
    lastNotes = Note.objects.filter(status='True').order_by('-id')[:10]
    randomNote = Note.objects.filter(status='True').order_by('?')[:6]
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
    setting = Setting.objects.get(pk=1)
    notes = Note.objects.filter(Category_id=id, status='True')
    category = Category.objects.all()
    categorydata=Category.objects.get(pk=id)
    context = {'notes': notes, 'category': category, 'categorydata':categorydata, 'setting': setting,}
    return render(request, 'notes.html', context)

def notes_all(request):
    setting = Setting.objects.get(pk=1)
    notes = Note.objects.filter(status='True')
    category = Category.objects.all()
    context = {'notes': notes, 'category': category, 'setting': setting}
    return render(request, 'notes_all.html', context)

def note_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    note = Note.objects.get(pk=id)
    images = Images.objects.filter(note_id=id)
    comments = Comment.objects.filter(note_id=id,status='True')
    context = {'category': category, 'comments':comments, 'note': note, 'images': images, 'setting': setting}
    return render(request, 'note_detail.html', context)

def note_search(request):
    setting = Setting.objects.get(pk=1)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                notes = Note.objects.filter(title__icontains=query,status='True')  # Select * from note where title like %query%
            else:
                notes = Note.objects.filter(title__icontains=query, Category_id=catid,status='True')   # Select * from note where title like %query%
            context = {'notes': notes,
                       'category': category,
                       'query': query,
                       'setting': setting
                       }
            return render(request,'note_search.html',context)
    return HttpResponseRedirect('/')


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        notes = Note.objects.filter(title__icontains=q,status='True')
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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Failed to Login!")
            return HttpResponseRedirect('/login/')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = { 'category': category, 'setting': setting}
    return render(request, 'login.html', context)


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "image/users/user.png"
            data.save()
            messages.success(request, "welcome "+current_user.first_name)
            return HttpResponseRedirect('/user/update/')
    form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = { 'category': category,
                'form': form,
                'setting': setting,
                }
    return render(request, 'register.html', context)


def faq(request):
    faq = FAQ.objects.filter( status='True').order_by('ordernumber')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'faq': faq, 'category': category, 'setting': setting}
    return render(request, 'faq.html', context)