from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import custom_model_form
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from account.forms import NewCommentForm
from .models import BlogPost, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count




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
    paginate_by = 5  # Number of comments per page
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        # Get all comments for the post and order them by date (most recent first)
        comments = post.comments.filter(status=True).order_by('-date')

        # Apply pagination to comments
        paginator = Paginator(comments, self.paginate_by)
        page_number = self.request.GET.get('page')

        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            # If page_number is not an integer, show the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. page_number > number of pages), show the last page
            page_obj = paginator.page(paginator.num_pages)

        total_comments = comments.count()  # Get the total number of comments
        context['comments'] = page_obj
        context['comment_form'] = NewCommentForm()
        context['total_likes'] = post.total_likes()
        context['liked'] = post.likes.filter(id=self.request.user.id).exists()
        context['total_comments'] = total_comments  # Add total_comments to the context
        return context



def add_comment(request, pk):
    post = get_object_or_404(models.BlogPost, pk=pk)
    comments = post.comments.filter(status=True)
    if request.method == "POST":
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.user = request.user
            user_comment.save()
            return redirect('index:blog_details', pk=pk)
    else:
        comment_form = NewCommentForm()
    return redirect('index:blog_details', pk=pk)



   


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
