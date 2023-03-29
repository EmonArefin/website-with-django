from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import *

from django.views.generic.edit import CreateView
from .forms import CommentForm
from django.urls import reverse_lazy
# from yourapp.models import Comment


# Create your views here.

def Home(request):
    template_name = 'home.html'
    return render(request, template_name)

def Blog(request):
    queryset = BlogPost.objects.filter(status = 'published').order_by('-created')
    per_page = 3
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    template_name = 'Blog/blog.html'
    context = {'posts':posts}
    return render(request, template_name, context)

def single_post(request, slug):
    post = get_object_or_404(BlogPost, slug= slug)
    template_name = 'Blog/single.html'
    context = {'post':post}
    return render(request, template_name, context)

# Comment Section
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    
    def form_valid(self, form, slug):
        post_id = self.kwargs.get('slug')
        form.instance.post_id = post_id
        return super().form_valid(form)
    success_url = reverse_lazy('home')

    
