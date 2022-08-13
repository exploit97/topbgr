from django.forms import ModelForm
from .models import  Subject,Es,Etablissement,Level,Year,Country,Evaluation,Matter,Category
from django import forms

   
    
class addSolutionForm(ModelForm):
    class Meta:
        model = Es
        fields = ['title','es_file',]
       
class addCountryForm(ModelForm):
    class Meta:

        model = Country
        fields = ['name',]
        

class addEtablissementForm(ModelForm):
    class Meta:

        model = Etablissement
        fields = ['name',]
        

class addLevelForm(ModelForm):
    class Meta:

        model = Level
        fields = ['name',]
        

class addMatterForm(ModelForm):
    class Meta:

        model = Matter
        fields = ['name',]
        

class addYearForm(ModelForm):
   class Meta: 

        model = Year
        fields = ['year',]
       

class addEvaluationForm(ModelForm):
    class Meta:

        model = Evaluation
        fields = ['name','description','image','category',]
        
class addCategoryForm(ModelForm):
    class Meta:

        model = Category
        fields = ['name',]
        