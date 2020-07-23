from django.shortcuts import render

def post_list(request):
    return render(request, 'wadachi_app/post_list.html', {})