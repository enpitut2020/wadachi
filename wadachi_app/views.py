from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def post_list(request):
    # いろいろ書く
    # 
    # データを取り出すクエリをかく
    posts = Post.objects.all()
    return render(request, 'wadachi_app/post_list.html', {'posts': posts})

@login_required
def post_new(request):
    if request.method == "POST":
        # POSTメソッドの時は渡されたデータをPostFormに格納
        form = PostForm(request.POST)
        if form.is_valid():
            # formに正当なデータが与えられたときの動作
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # 登録完了後に行う操作
            # この場合はpost_list(トップページ)にリダイレクト
            return redirect('post_list')

            # return redirect('post_detail', pk=post.pk)
    else:
        # GETメソッドの時はカラのformを用意する
         form = PostForm()
    return render(request, 'wadachi_app/forms.html', {'form': form})
    