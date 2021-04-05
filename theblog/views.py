from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, UpdatePostForm, CommentForm
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect

# Create your views here.
def about(request):
    return render(request, 'about.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_at']

class ArticleView(DetailView, CreateView):
    model = Post
    form_class = CommentForm
    template_name = 'article.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleView, self).get_context_data()
        post = Post.objects.get(id=self.kwargs['pk'])
        title = post.title
        body = post.body
        author_id = post.author.id
        author_fname = post.author.first_name
        author_lname = post.author.last_name
        post_id = post.id
        created_at = post.created_at
        comments = reversed(post.comments.all())
        comments_count = len(post.comments.all())
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        context['total_likes'] = total_likes
        context['body'] = body
        context['author_id'] = author_id
        context['title'] = title
        context['created_at'] = created_at
        context['post_id'] = post_id
        context['comments'] = comments
        context['author_fname'] = author_fname
        context['author_lname'] = author_lname
        context['comments_count'] = comments_count
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

# class AddCommentView(CreateView):
#     model = Comment
#     template_name = 'article.html'
#     fields = '__all__'