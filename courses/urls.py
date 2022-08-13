from django.urls import path
from django.contrib.auth.decorators import login_required

from courses.views import HomeView,HistoryView,AboutView,ContactView,CourseListView, CourseDetailView,LessonDetailView, SearchView, create_classe, create_subject, create_teaching

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('history/', HistoryView.as_view(), name='history'),
    path('courses/<int:category>', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()), name='course_detail'),
    path('courses/<course_slug>/<lesson_slug>/', login_required(LessonDetailView.as_view()), name='lesson_detail'),
    path('search/', SearchView, name='search_result'),
    path('create/classe', create_classe, name='create_classe'),
    path('create/subject', create_subject, name='create_subject'),
    path('create/teaching', create_teaching, name='create_teaching')

]
