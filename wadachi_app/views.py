from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BridgeForm, BrickForm
from .models import Bridge, Brick
from django.utils import timezone
from .models import Bridge

import django.http
from . import forms
import re

from django.db.models import Q

# user signin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def post_list(request):
    # posts = Brick.objects.all()
    # return render(request, 'wadachi_app/post_list.html', {'posts': posts})
    pass  # 関数の内容がないので一時的に書いてます

def bridge_list(request):
    q_word = request.GET.get('query')
    if q_word:
        object_list = Bridge.objects.filter(
            Q(topic__icontains=q_word) |
            Q(contributor__username__icontains=q_word) |
            Q(context__icontains=q_word) |
            Q(goal__icontains=q_word))
        search_mode = True
    else:
        object_list = Bridge.objects.all()
        search_mode = False
    return render(request, 'wadachi_app/bridge_list.html', {'bridges': object_list, 'search_mode': search_mode})

def brick_list(request, pk):
    bricks = Brick.objects.filter(bridge__pk=pk)
    bridge = Bridge.objects.get(id=pk)
    return render(request, 'wadachi_app/brick_list.html',
            {'bricks': bricks, 'bridge': bridge})

@login_required
def brick_new(request, pk):
    if request.method == "POST":
        # POSTメソッドの時は渡されたデータをPostFormに格納
        form = BrickForm(request.POST)
        if form.is_valid():
            # formに正当なデータが与えられたときの動作
            brick = form.save(commit=False)
            # request.userは正しいか??
            brick.published_date = timezone.now()
            brick.bridge = Bridge.objects.get(id=pk)
            brick.save()
            # 登録完了後に行う操作
            # この場合はbrick_list(bridgeのページ)にリダイレクト
            return redirect('brick_list', pk=pk)

            # return redirect('post_detail', pk=post.pk)
    else:
        # GETメソッドの時はカラのformを用意する
         form = BrickForm()
         # forms.html 変える必要あり??
    return render(request, 'wadachi_app/forms.html', {'form': form})

@login_required
def bridge_new(request):
    if request.method == "POST":
        # POSTメソッドの時は渡されたデータをPostFormに格納
        form = BridgeForm(request.POST)
        if form.is_valid():
            # formに正当なデータが与えられたときの動作
            bridge = form.save(commit=False)
            # contributor = user
            bridge.contributor = request.user
            bridge.save()
            # 登録完了後に行う操作
            # bridge_list(トップページ)にリダイレクト
            return redirect('bridge_list')

            # return redirect('post_detail', pk=post.pk)
    else:
        # GETメソッドの時はカラのformを用意する
        form = BridgeForm()
    return render(request, 'wadachi_app/forms.html', {'form': form})

def has_digit(text):
    if re.search("\d", text):
        return True
    return False

def has_alphabet(text):
    if re.search("[a-zA-Z]", text):
        return True
    return False

def registation_user(request):
    if request.method == 'POST':
        registration_form = forms.RegistrationForm(request.POST)
        password = request.POST['password']
        if len(password) < 8:
            registration_form.add_error('password', "文字数が8文字未満です。")
        if not has_digit(password):
            registration_form.add_error('password',"数字が含まれていません")
        if not has_alphabet(password):
            registration_form.add_error('password',"アルファベットが含まれていません")
        if registration_form.has_error('password'):
            return render(request, 'registration.html', {'registration_form': registration_form})
        user = User.objects.create_user(username=request.POST['username'], password=password)
        # user = User.objects.create_user(username=request.POST['username'], password=password, email=request.POST['email'])
        return django.http.HttpResponseRedirect('/')
    else:
        registration_form = forms.RegistrationForm()
    return render(request, 'registration.html', {'registration_form': registration_form})
