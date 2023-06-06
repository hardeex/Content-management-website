from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import custom_model_form
from django.urls import reverse_lazy
#from django.shortcuts import redirect
#from django.conf.urls import handler404
#from django.conf import settings



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
    #jobs = models.JobPost.objects.all()[:5]
    #blogs = models.BlogPost.objects.all()[:5]
    blogs = models.BlogPost.objects.order_by('-date')[:5]
    jobs = models.JobPost.objects.order_by('-pushlished_date')[:5]
    return render(request, 'home/home.html',{
        'jobs': jobs,
        'blogs': blogs
    })

def CategoryView(request, category_name):
    try:
        #category = models.BlogPost.objects.filter(category='category_name')
        category = models.BlogCategory.objects.get(name=category_name)
        posts = models.BlogPost.objects.filter(category=category)
        return render(request, 'home/category_view.html', {
            'category': category,
            'posts': posts
        })
    except models.BlogCategory.DoesNotExist:
        return render(request, 'home/category_not_found.html')
    except:
        return render(request, 'home/error.html')


#def PageNotFound(request, exception):
 #   return render(request, 'home/error.html', status=404)

#def reddirct_to_error_page(request, exception):
 #   return render(request, 'home/error.html')