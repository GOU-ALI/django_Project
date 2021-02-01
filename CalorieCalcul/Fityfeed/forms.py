from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class fooditemForm(ModelForm):
    class Meta:
        model=Fooditem
        fields="__all__"

class addUserFooditem(ModelForm):
    class Meta:
        model=UserFooditem
        fields="__all__"

class createUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
#Above mentioned code is required to create, update models which we have created earlier in models.py (for CRUD functionality)
