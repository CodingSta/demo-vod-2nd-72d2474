from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post


def post_new(request):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'  # CreateView CBV의 Rule대로 지정한 것
    success_url = '/'

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(success_url)
    else:
        form = form_cls()

    return render(request, template_name, {
        'form': form,
    })
