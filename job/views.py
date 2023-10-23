from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import job_forms
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from . job_forms import NewCommentForm
from .models import JobPost, JobComment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin





# create classes the views
class JobHomeView(ListView):
    model = models.JobPost
    template_name = 'jobs/job_list.html'
    ordering = ['-date']



class JobDetailsView(DetailView): 
    model = models.JobPost
    template_name = 'jobs/job_details.html'
    context_object_name = 'post'
    paginate_by = 5  # Number of comments per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        # Get all comments for the post and order them by date (most recent first)
        comments = post.job_comments.filter(status=True).order_by('-date')
        total_comments = comments.count()  # Get the total number of comments

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

        # Passing the data to the page context
        context['comments'] = page_obj
        context['comment_form'] = NewCommentForm()
        context['total_comments'] = total_comments  # Add total_comments to the context
        return context




def add_job_comment(request, pk):
    post = get_object_or_404(models.JobPost, pk=pk)
    comments = post.job_comments.filter(status=True)
    if request.method == "POST":
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.user = request.user
            user_comment.save()
            return redirect('jobs:job_details', post.pk)
    else:
        comment_form = NewCommentForm()
    return redirect('jobs:job_details', post.pk)






class AddJobPostView(CreateView):
    model = models.JobPost
    form_class = job_forms.CustomJobPostForm
    template_name = 'jobs/add_job_post.html'
    #fields = '__all__'


class AddJobCategoryView(CreateView):
    model = models.JobCategory
    template_name = 'jobs/add_job_category.html'
    fields = '__all__'



class EditJobPostView(UpdateView):
    model = models.JobPost    
    template_name = 'jobs/edit_job_post.html'
    form_class = job_forms.CustomJobPostForm
    

class DeleteJobPostView(DeleteView):
    model = models.JobPost
    success_url = reverse_lazy('jobs:job_list')
    template_name = 'jobs/delete_job_post.html'
    
    

# Create the function views here.

def JobCategoryView(request, category_name):
    try:      
        category = models.JobCategory.objects.get(name=category_name)       
        posts = models.JobPost.objects.filter(category=category)   
        return render(request, 'jobs/category_job_view.html', {
            'category': category,
            'posts': posts,            
        })
    except models.JobCategory.DoesNotExist:
        return render(request, 'home/category_not_found.html')
    except:
        return render(request, 'home/error.html')


def ListJobCategory(request):
    category_list = models.JobCategory.objects.all()    
    return render(request, 'jobs/job_category_list.html', {
            'category_list': category_list            
    })



# creating the code that save job post as a draft before publishing
class JobDraftsListView(LoginRequiredMixin, ListView):
    model = models.JobSaveAsDraft
    template_name = 'jobs/job_draft_list.html'
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(author=user)



class AddJobDraftPostView(CreateView):
    model = models.JobSaveAsDraft
    form_class = job_forms.JobDraftPostForm
    template_name = 'jobs/save_job_as_draft.html'


    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)


class JobDraftPostDetailsView(DetailView):
    model = models.JobSaveAsDraft
    template_name = 'jobs/drafts_job_details.html'    
   


def publish_job_draft(request, job_draft_pk):
    job_draft = get_object_or_404(models.JobSaveAsDraft, pk=job_draft_pk)
    
    # Create a new BlogPost instance
    job_post = models.JobPost(
        author=job_draft.author,
        title=job_draft.title,
        date= job_draft.date,
        location=job_draft.location,
        category=job_draft.category,
        content=job_draft.content
    )
    # save the draft to the job post model-- published
    job_post.save()
    
    # Delete the draft post
    job_draft.delete()
    
    return redirect('jobs:job_list')  # Redirect to the blog post list page




class EditJobDraftPostView(UpdateView):
    model = models.JobSaveAsDraft
    template_name = 'jobs/edit_job_draft_post.html'
    form_class = job_forms.JobDraftPostForm



    

class DeleteJobDraftPostView(DeleteView):
    model = models.JobSaveAsDraft
    success_url = reverse_lazy('jobs:job_drafts_list')
    template_name = 'jobs/delete_job_draft_post.html'
    