from django.shortcuts import render, redirect
from .forms import BridgeForm, BrickForm
from .models import Bridge, Brick
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def post_list(request):
    # posts = Brick.objects.all()
    # return render(request, 'wadachi_app/post_list.html', {'posts': posts})
    pass  # 関数の内容がないので一時的に書いてます

def bridge_list(request):
    bridge = Bridge.objects.all()
    return render(request, 'wadachi_app/bridge_list.html', {'bridges': bridge})

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
