from django.contrib import admin
from .models import SignUpModel,Login,ContactModel

# Register your models here.
@admin.register(SignUpModel)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','First_Name','Last_Name','Email','Phone_No','Password']

@admin.register(Login)
class UserLogin(admin.ModelAdmin):
    list_display=['email','password']

@admin.register(ContactModel)
class ContactDeatil(admin.ModelAdmin):
    list_display=['your_name','working_mail','company_website','feed_back']

