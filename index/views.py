from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import custom_model_form
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from account.forms import CommentForm
#from ckeditor.fields import RichTextField
#from django.shortcuts import redirect
#from django.conf.urls import handler404
#from django.conf import settings

from .models import BlogPost, Comment

# create classes the views
class JobHomeView(ListView):
    model = models.JobPost
    template_name = 'home/job_list.html'
    ordering = ['-pushlished_date']
    


class JobDetailsView(DetailView):
    model = models.JobPost
    template_name = 'home/job_details.html'


class BlogHomeView(ListView):
    model = models.BlogPost
    template_name = 'home/blog_list.html'
    ordering = ['-date']
  


class BlogDetailsView(DetailView):
    model = models.BlogPost
    template_name = 'home/blog_details.html'

    def get_context_data(self, *args, **kwargs):
        get_likes = get_object_or_404(models.BlogPost, id=self.kwargs['pk'])
        context = super(BlogDetailsView, self).get_context_data(*args, **kwargs)
        total_likes = get_likes.total_likes()    
        
        liked = False    
        if get_likes.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked']=liked
        context['comment_form'] = CommentForm()  # Add the comment form to the context
        return context


class AddPostView(CreateView):
    model = models.BlogPost
    form_class = custom_model_form.CustomBlogPostForm
    template_name = 'home/add_post.html'
    #fields = '__all__'


class AddCategoryView(CreateView):
    model = models.BlogCategory
    #form_class = custom_model_form.CustomBlogPostForm
    template_name = 'home/add_category.html'
    fields = '__all__'



class EditPostView(UpdateView):
    model = models.BlogPost
    #fields = ['title', 'content']
    template_name = 'home/edit_post.html'
    form_class = custom_model_form.CustomBlogPostForm
    #success_url = 'home/blog_details.html'

class DeletePostView(DeleteView):
    model = models.BlogPost
    success_url = reverse_lazy('index:blog_list')
    template_name = 'home/delete_post.html'
    
    

# Create the function views here.
def home(request):
    try:
            #jobs = models.JobPost.objects.all()[:5]
            #blogs = models.BlogPost.objects.all()[:5]
            blogs = models.BlogPost.objects.order_by('-date')[:5]
            jobs = models.JobPost.objects.order_by('-pushlished_date')[:5]
            return render(request, 'home/home.html',{
                'jobs': jobs,
                'blogs': blogs
            })  
    except:
        return render(request, 'home/error.html')

def CategoryView(request, category_name):
    try:
        #category = models.BlogPost.objects.filter(category='category_name')
        category = models.BlogCategory.objects.get(name=category_name)       
        posts = models.BlogPost.objects.filter(category=category)   
        return render(request, 'home/category_view.html', {
            'category': category,
            'posts': posts,            
        })
    except models.BlogCategory.DoesNotExist:
        return render(request, 'home/category_not_found.html')
    except:
        return render(request, 'home/error.html')


def ListCategory(request):
    category_list = models.BlogCategory.objects.all()    
    return render(request, 'home/category_list.html', {
            'category_list': category_list            
    })

def LikeView(request, pk):
    post = get_object_or_404(models.BlogPost, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        lked= False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('index:blog_details', args=[str(pk)]))




def add_comment(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blogpost
            comment.save()
            return redirect('home:blog_details', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'home/add_comment.html', {'form': form})
