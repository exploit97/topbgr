from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post, Categorie, Comment
from django.utils import timezone
from blog.forms import PostForm,AddCommentForm,AddCategorieForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView )
from django.contrib import messages
from django.http import HttpResponseRedirect
from users.models import Profile
from examen_et_concours.models import Category
from courses.models import Classe

# Create your views here.

    
    
def home(request):
    categories = Categorie.objects.all()[:6]
    conc_categories = Category.objects.all()
    courses = Classe.objects.all()
    
    posts = Post.objects.order_by('-created_date')[:3]
    context = {'categories':categories,
    'conc_categories':conc_categories,

         'courses' :courses,      
                'posts':posts }
    return render(request,'home.html',context)
    
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    ordering = ['-created_date']

    def get_context_data(self,*args,**kwargs):
        categorie_menu = Categorie.objects.all()
        context=super(PostListView,self).get_context_data(*args,**kwargs) 
        context['categorie_menu'] = categorie_menu
       
        return context 
    

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    
    def get_context_data(self,*args,**kwargs):
        categorie_menu = Categorie.objects.all()
        posts = Post.objects.all()
        context=super(PostDetailView,self).get_context_data(*args,**kwargs) 
        stuff = get_object_or_404(Post, id= self.kwargs['pk'])
        total_likes = stuff.total_likes() 
        Liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            Liked =True
        context['categorie_menu'] = categorie_menu
        context['total_likes'] = total_likes
        context['Liked'] = Liked
        context['posts'] = posts
        return context 

class CreatePostView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    form_class = PostForm
    

    def form_valid(self,form):
        
        form.instance.author = self.request.user
        
        return super().form_valid(form)

            
def delete_post(request, id):
    Post(id = id).delete()
    return redirect('blogs:post_list')


class UpdatePostView(UpdateView):
    model = Post
    template_name= 'blog/update_post.html'
    form_class = PostForm


class AddCategorieView(CreateView):

    model = Categorie
    template_name = 'blog/add_categorie.html'
    #form_class = AddCategorieForm
    fields = '__all__'
    success_url = reverse_lazy('blogs:create_post')


class AddCommentView(CreateView):

    model = Comment
    template_name = 'blog/add_comment_section.html'
    form_class = AddCommentForm
    #fields = '__all__'
    success_url = reverse_lazy('blogs:post_list')

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

def sameCategorieList(request, cats):
    categorie = get_object_or_404(Categorie, name = cats)
    posts = Post.objects.all()
    categorie_posts = categorie.post_set.all()
    context = {'cats':cats.title().replace('-',' '), 
               'categorie_posts':categorie_posts,
               'posts':posts,
               }

    return render(request,'blog/same_categorie_list.html', context)
    
def categorieListView(request):
     categorie_list_view = Categorie.objects.all()
     return render(request,'blog/categorie_list.html', {'categorie_list_view':categorie_list_view}) 

def like_view(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    Liked = False
    if post.likes.filter(id = request.user.id).exists() :
        post.likes.remove(request.user.id)
        Liked = False
    else :
         post.likes.add(request.user)
         Liked = True
    return HttpResponseRedirect(reverse('blogs:post_detail', args = str(pk)))
    

class showProfileView(DetailView):
    model = Profile
    template_name ='blog/showProfileView.html'

    def get_context_data(self,*args,**kwargs):
        
        user_page = get_object_or_404(Profile, id= self.kwargs['pk'])
        context = super(showProfileView,self).get_context_data(*args,**kwargs)
        context['user_page'] = user_page
        return context
