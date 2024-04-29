from django.contrib import admin
from .models import Data,BMI_Calculater,Gallery,Post,Auther,Tag,Video

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_filter =("auther","tag","date",)
    list_display =("title","date","auther")



admin.site.register(Data)
admin.site.register(BMI_Calculater)
admin.site.register(Gallery)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Auther)
admin.site.register(Video)

