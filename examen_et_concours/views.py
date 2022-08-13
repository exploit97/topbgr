from django.shortcuts import render, get_object_or_404
from .models import Es, Evaluation, Category, Subject,Level,Matter,Country,Year,Etablissement
from django.views.generic import ListView, UpdateView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy,reverse
from .forms import addEvaluationForm,addCountryForm,addEtablissementForm,addLevelForm,addSolutionForm,addYearForm,addMatterForm,addCategoryForm
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from memberships.models import UserMembership
from memberships.views import get_user_membership
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# Create your views here.



class ToutesLesEvaluations(ListView):
    template_name='examen_et_concours/evaluations.html'
    model = Category
    paginate_by = 6

class ConcoursDescription(DetailView):
    template_name='examen_et_concours/concours_description.html'
    model = Evaluation
   
class concoursSubject(DetailView):
    template_name='examen_et_concours/concours_matters.html'
    model = Evaluation

def SubjectsView(request,eval,matter,level):

    mat = Matter.objects.filter(id=matter)
    lev = Level.objects.filter(id=level)
    ev = Level.objects.filter(id=eval)
    subject = Subject.objects.filter(matter=matter).filter(evaluation=eval).filter(level=level)
    
    context = {'subject':subject,
    'mat':mat,

         'lev' :lev,      
                'ev':ev }
    return render(request,'examen_et_concours/subjects.html',context)
    


class SubjectView(DetailView):
    template_name='examen_et_concours/subject.html'
    model = Subject 

    
    def get_context_data(self,*args,**kwargs):
        user_membership = UserMembership.objects.get(id=self.request.user.id)
        user_membership_type = user_membership.membership.membership_type
        
        sujet = get_object_or_404(Subject, id= self.kwargs['pk'])
        es = sujet.es

        context=super(SubjectView,self).get_context_data(*args,**kwargs) 
        es_allowed_mem_types = es.allowed_memberships
        es_allowed_mem_types = es_allowed_mem_types.all()

        context['es'] = None
        

        if es_allowed_mem_types.filter(membership_type=user_membership_type).exists():
         context['es'] = es
       
        return context 



class AddSubjectView(CreateView):

    model = Subject
    template_name = 'examen_et_concours/add_subject.html'
    #form_class = AddsubjectForm
    fields = '__all__'
    success_url = reverse_lazy('examen_et_concours:touslesconcours')
     
class addConcours(CreateView):
    model = Evaluation
    form_class=addEvaluationForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addLevel(CreateView):
    model = Level
    form_class=addLevelForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addMatter(CreateView):
    model = Matter
    form_class=addMatterForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addYear(CreateView):
    model = Year
    form_class=addYearForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addCountry(CreateView):
    model = Country
    form_class=addCountryForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addCategory(CreateView):
    model = Category
    form_class=addCategoryForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')

class addSolution(CreateView):
    model = Es
    form_class=addSolutionForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')


class addEtablissement(CreateView):
    model = Etablissement
    form_class=addEtablissementForm
    template_name = 'examen_et_concours/add.html'
    success_url = reverse_lazy('examen_et_concours:add_subject')
    

            
                    
         
       