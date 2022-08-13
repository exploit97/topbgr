from django import forms
from blog.models import Post, Categorie,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model= Post
        fields = ['title','text','categorie','snippet']
        widgets = {
            'title': forms.TextInput(attrs={"class":'form-control' ,'name':'title'}),
        'text' : forms.Textarea(attrs={'class':"form-control", 'name':"text", 'cols':"30" ,'rows':"10" }),
        'snippet' : forms.Textarea(attrs={'class':"form-control", 'name':"snippet", 'cols':"30" ,'rows':"5" }),
        'categorie' : forms.Select(attrs={'class':"form-control", 'name':"categorie" }),
        } 
    

class AddCommentForm(forms.ModelForm):

    class Meta:
        model= Comment
        fields = ['name','text']
        widgets = {
            'name': forms.TextInput(attrs={"class":'form-control' ,'name':'name'}),
        'text' : forms.Textarea(attrs={'class':"form-control", 'name':"text", 'cols':"30" ,'rows':"10" }),
        
        } 

class AddCategorieForm(forms.ModelForm):

    class Meta:
        model= Categorie
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={"class":'form-control' ,'name':'name'}),
            
        
        
        } 