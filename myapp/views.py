from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm, CommentForm
from .models import Post, Comment


post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)


def post_new(request):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'  # CreateView CBV의 Rule대로 지정한 것
    success_url = '/'

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, '새 글을 저장했습니다.')
            return redirect(success_url)
    else:
        form = form_cls()

    return render(request, template_name, {
        'form': form,
    })


def post_edit(request, pk):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'  # CreateView CBV의 Rule대로 지정한 것
    success_url = '/'

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '글을 수정/저장했습니다.')
            return redirect(success_url)
    else:
        form = form_cls(instance=post)

    return render(request, template_name, {
        'form': form,
    })


def comment_new(request, post_pk):
    form_cls = CommentForm
    template_name = 'myapp/comment_form.html'
    success_url = '/'

    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)  # author, message
            comment.post = post
            comment.ip = request.META['REMOTE_ADDR']
            comment.save()
            messages.success(request, '새 댓글을 저장했습니다.')
            return redirect(success_url)  # post_detail
    else:
        form = form_cls()

    return render(request, template_name, {
        'form': form,
    })


def comment_edit(request, post_pk, pk):
    form_cls = CommentForm
    template_name = 'myapp/comment_form.html'
    success_url = '/'

    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            messages.success(request, '댓글을 수정/저장했습니다.')
            return redirect(success_url)  # TODO: post detail
    else:
        form = form_cls(instance=comment)

    return render(request, template_name, {
        'form': form,
    })
