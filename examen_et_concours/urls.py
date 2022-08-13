from django.urls import path, include
from  examen_et_concours import views
from django.contrib.auth.decorators import login_required

app_name = 'examen_et_concours'
urlpatterns = [
    
    path('evaluations/liste', views.ToutesLesEvaluations.as_view(),name='touslesconcours'),
    path('concours/description/<int:pk>/', views.ConcoursDescription.as_view(),name='concours_description'),
    path('concours/<int:pk>/', views.concoursSubject.as_view(),name='concours_matters'),
    path('concours/sujets/<int:eval>/<int:matter>/<int:level>/', views.SubjectsView,name='subjects'),
    path('sujets/<int:pk>/', login_required(views.SubjectView.as_view()),name='subject'),
    path('examens/sujets/addsubject',views.AddSubjectView.as_view() , name='add_subject'),
    path('examens/sujets/add_category',views.addCategory.as_view(), name='add_category'),
    path('examens/sujets/add_solution',views.addSolution.as_view(), name='add_solution'),
    path('examens/sujets/add_year',views.addYear.as_view(), name='add_year'),
    path('examens/sujets/add_country',views.addCountry.as_view(), name='add_country'),
    path('examens/sujets/add_level',views.addLevel.as_view(), name='add_level'),
    path('examens/sujets/add_matter',views.addMatter.as_view(), name='add_matter'),
    path('examens/sujets/add_etablissement',views.addEtablissement.as_view(), name='add_etablissement'),
    path('examens/sujets/add_examen',views.addConcours.as_view(), name='add_examen'),
   

]


