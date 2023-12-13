from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm

class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    

class ChangeData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']