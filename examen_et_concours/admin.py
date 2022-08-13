from django.contrib import admin
from .models import Evaluation, Category,Es, Subject,Matter,Level,Country,Etablissement,Year

# Register your models here.




admin.site.register(Subject)
admin.site.register(Es)
admin.site.register(Evaluation)
admin.site.register(Category)
admin.site.register(Level)
admin.site.register(Country)
admin.site.register(Matter)
admin.site.register(Etablissement)
admin.site.register(Year)

