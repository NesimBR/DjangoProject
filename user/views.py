from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from home.models import UserProfile, Setting
from note.models import Category, Comment, Note, Images
from user.forms import UserUpdateForm, ProfileUpdateForm
from user.models import NoteForm, NoteImageForm


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile,
               'setting': setting,
               }
    return render(request, 'user_profile.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'ok')
            return redirect('/user')

    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'setting': setting,
        }
        return render(request, 'user_update.html', context)


def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'ok')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'ERROR<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')

    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form': form,
            'category': category,
            'setting': setting
        })


@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user)
    context = {
        'category': category,
        'comments': comments,
        'setting': setting,
    }
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')
def deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'comment deleted')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')
def notes(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    note = Note.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'note': note,
        'setting': setting,
    }
    return render(request, 'user_notes.html', context)


@login_required(login_url='/login')
def addnote(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Note()
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.description = form.cleaned_data['description']
            data.keywords = form.cleaned_data['keywords']
            data.image = form.cleaned_data['image']
            data.detail = form.cleaned_data['detail']
            data.slug = form.cleaned_data['slug']
            data.status = 'New'
            catid = form.cleaned_data['Category']
            data.Category_id = catid.id
            data.save()
            messages.success(request, "Your Note has been Added")
            return HttpResponseRedirect('/user/notes')
        else:
            messages.warning(request, "Note Field" + str(form.errors))

            return HttpResponseRedirect('/user/notes')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        form = NoteForm()
        context = {
            'category': category,
            'form': form,
            'setting': setting,
        }
        return render(request, 'user_addnote.html', context)


@login_required(login_url='/login')
def notedelete(request, id):
    current_user = request.user
    Note.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Note Deleted...')
    return HttpResponseRedirect('/user/notes')


@login_required(login_url='/login')
def noteEdit(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Note has been updated")
            return HttpResponseRedirect('/user/notes')
        else:
            messages.warning(request, "Note Field" + str(form.errors))

            return HttpResponseRedirect('/user/noteEdit/'+str(id))
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        form = NoteForm(instance=note)
        context = {
            'category': category,
            'form': form,
            'setting': setting
        }
        return render(request, 'user_addnote.html', context)


def noteaddimage(request,id):
    if request.method == 'POST':
        lasturl = request.META.get('HTTP_REFERER')
        form = NoteImageForm(request.POST,request.FILES)
        if form.is_valid():
            data = Images()
            data.title = form.cleaned_data['title']
            data.note_id = id
            data.image = form.cleaned_data['image']
            data.save()
            messages.success(request, "Image has been uploaded")
            return HttpResponseRedirect(lasturl)
        else:
            messages.warning(request, "Form ERROR" + str(form.errors))
            return HttpResponseRedirect(lasturl)
    else:
        note = Note.objects.filter(id=id)
        images = []
        images = Images.objects.filter(note_id=id)
        form = NoteImageForm()
        context = {
            'note': note,
            'images': images,
            'form': form,
        }
    return render(request, 'note_gallery.html', context)
