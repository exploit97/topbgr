from django.urls import path
from blog.views import PostListView,PostDetailView,home, CreatePostView, delete_post,showProfileView, UpdatePostView,AddCategorieView,sameCategorieList,categorieListView,like_view,AddCommentView

app_name = 'blogs'

urlpatterns = [
    path("",home,name='home'),
    path('blog/',PostListView.as_view(),name='post_list'),
    path('blog/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('blog/create/', CreatePostView.as_view(), name='create_post'),
    path('blog/<int:id>/delete/', delete_post, name='delete_post'),
    path('blog/update/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('blog/add_categorie/', AddCategorieView.as_view(), name='add_categorie'),
    path('blog/categorie/<str:cats>/', sameCategorieList, name='same_categorie_list'),
    path('blog/categorie_list/', categorieListView, name='categorie_list'),
    path('blog/like/<int:pk>', like_view, name='like_view'),
    path('blog/<int:pk>/add_comment/',AddCommentView.as_view(), name ='add_comment_section'),
    path('blog/<int:pk>/author_profile', showProfileView.as_view(), name='showProfileView')
    


]