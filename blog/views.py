from datetime import date
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_list_or_404
from django.http import Http404,HttpResponseRedirect
from .models import Post,Tag,Author
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from django.views import View
from .forms import CommentForm
from django.urls import reverse

all_posts = Post.objects.all()


# class starting_page(View):
#     def get(self,request):
#         latest_posts = Post.objects.all().order_by("-date")[:3]
#         return render(request, "blog/index.html",{
#         "posts":latest_posts,
#     })

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    
    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data
    
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"
    
# class posts(View):
#     def get(self,request):
#         return render(request, "blog/all-posts.html",{
#         "all_posts": all_posts,
#     })
        

# class SinglePostView(View):
#     def get(self,request,slug):
#         identified_post = Post.objects.get(slug = slug)
#         context = {
#             "post":identified_post,
#             "post_tags":identified_post.tags.all(),
#             "comment_form" :CommentForm(),
#         }
#         return render(request, "blog/post-detail.html",context)

    
# class SinglePostView(DetailView):
#     template_name = "blog/post-detail.html"
#     model = Post
    
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         # slug = kwargs["slug"] #that's happening auto by django
#         # identified_post = Post.objects.get(slug = slug)
#         # context["post"] = identified_post
#         context["comment_form"] = CommentForm()
#         context["post_tags"] = self.object.tags.all()
#         context["comments"] = self.object.comments.all()
#         return context
    
class SinglePostView(View):
    def get(self,request,slug):
        post = Post.objects.get(slug = slug)
        context = {
            "post":post,
            "post_tags": post.tags.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id")
        }
        return render(request,"blog/post-detail.html",context)
    def post(self,request,slug):
        selected_post = Post.objects.get(slug = slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comments = comment_form.save(commit=False)
            comments.post = selected_post #post from the model to be updated as a confirmation that it's linked correctly to the comment 
            comments.save()
            return HttpResponseRedirect(reverse("post_detail_page", args=[slug]))
        else:
            post = Post.objects.get(slug = slug)
        context = {
            "post":post,
            "post_tags": post.tags.all(),
            "comment_form":CommentForm,
            "comments":post.comments.all().order_by("-id")

        }
        return render(request,"blog/post-detail.html",context)
    
class ReadLaterView(View):
    
    def get(self,request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_stored"] = False
        else:
            stored_posts = Post.objects.filter(id__in = stored_posts)
            context["posts"] = stored_posts
            context["has_stored"] = True
        return render(request, "blog/stored-posts.html",context)
        
    def post(self,request):
        stored_posts = request.session.get("stored_posts") #this is the syntax to fetch data from session 
        if stored_posts is None:
            stored_posts = []
        post_id =  int(request.POST["post_id"]) #here we need to call request.POST to get the value from the post
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"]= stored_posts
            
        return HttpResponseRedirect("/")
            

        
