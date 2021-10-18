from django.views.generic import TemplateView, ListView, DetailView

from .models import Post


class IndexView(TemplateView):
    template_name = 'index.html'


class PostListView(ListView):
    queryset = Post.objects.order_by('-pub_date')
    template_name = 'blog/blog.html'


class PostDetailView(DetailView):
    model = Post
