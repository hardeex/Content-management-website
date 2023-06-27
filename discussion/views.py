from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from job.job_forms import NewCommentForm
from . forms import NewCommentForm
from . import forms
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
#from account.forms import NewCommentForm
from .models import Discussion, Comment
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count



# create classes the views
class DiscussionHomeView(ListView):
    model = models.Discussion
    template_name = 'discussion/discuss_list.html'
    ordering = ['-date']



class DiscussionDetailsView(DetailView):
    model = models.Discussion
    template_name = 'discussion/discuss_details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        # Get all comments for the post and order them by date (most recent first)
        comments = post.discuss_comments.filter(status=True).order_by('-date')

        total_comments = comments.count()  # Get the total number of comments
        #context['comments'] = page_obj
        context['comments'] = comments
        context['comment_form'] = NewCommentForm()
        context['total_likes'] = post.total_likes()
        context['liked'] = post.likes.filter(id=self.request.user.id).exists()
        context['total_comments'] = total_comments  # Add total_comments to the context
        return context



def add_discussion_comment(request, pk):
    post = get_object_or_404(models.Discussion, pk=pk)
    comments = post.discuss_comments.filter(status=True)
    if request.method == "POST":
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.user = request.user
            user_comment.save()
            return redirect('discussion:discuss_details', pk=pk)
    else:
        comment_form = NewCommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'total_likes': post.total_likes(),
        'liked': post.likes.filter(id=request.user.id).exists(),
        'total_comments': comments.count(),
    }
    return render(request, 'discussion/discuss_details.html', context)





class CreateDiscussionView(CreateView):
    model = models.Discussion
    form_class = forms.DiscussionForm
    template_name = 'discussion/create_discussion_post.html'
    #fields = '__all__'



class EditDiscussionPostView(UpdateView):
    model = models.Discussion   
    template_name = 'discussion/edit_discussion_post.html'
    form_class = forms.DiscussionForm
    #success_url = 'discussion/discuss_details.html'



class DeleteDiscussionPostView(DeleteView):
    model = models.Discussion
    success_url = reverse_lazy('discussion:discuss_list')
    template_name = 'discussion/delete_discuss_post.html'
    
    

# Create the function views here.
def DiscussionLikeView(request, pk):
    post = get_object_or_404(models.Discussion, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        lked= False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('discussion:discuss_details', args=[str(pk)]))
