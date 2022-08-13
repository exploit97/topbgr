from django import forms
from django.contrib.auth.models import User
from .models import Classe, Sujets, Lesson



class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = '__all__'
        help_texts = {
            'title': 'Par exemple. Classe 11 ou classe d\'informatique',
            'description':'Mettez une brève description de la classe',
            'image':'Vous pouvez mettre une photo de la classe ou elle peut être laissée vide'
        }

class SujetsForm(forms.ModelForm):
    class Meta:
        model = Sujets
        fields = ['creator','slug', 'title', 'classe', 'description', 'course_image']
        help_texts = {
            'title': 'Exemple. Mathématiques, géographie, etc.',
            'description': 'Mettre une brève description du sujet',
            'classe': 'Sélectionnez la classe pour laquelle vous allez créer le sujet',
            'subject_image': 'Vous pouvez télécharger une photo du sujet ou la laisser vide'
        }
        labels = {
            'title':'Titre du sujet'
        }
        widgets = {'creator': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','title', 'subject', 'video_id', 'position', ]
        help_texts = {
            'title': 'Entrez le titre de la leçon',
            'subject': 'Choisissez le sujet auquel appartient cette leçon',
        
            'position': 'Entrez le numéro de position ou la file d\'attente',
            'video_id': 'Saisissez l\'ID vidéo de Youtube à mettre en ligne (<a href="/static/images/youtube_help.png"> où puis-je trouver l\'ID de la video</a>) '
        }
        widgets = {
            'slug': forms.HiddenInput()
        }