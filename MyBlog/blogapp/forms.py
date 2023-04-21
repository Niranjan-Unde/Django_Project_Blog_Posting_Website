
from django import forms
from . models import Post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    # cat=forms.ChoiceField(choices=CHOICES)
    statusChoices=(('1','Active'),('0','Inactive'))
    status=forms.ChoiceField(initial='1',widget=forms.RadioSelect(attrs={'class':'custom-control-input'}),choices=statusChoices)
    class Meta:
        model = Post
        fields = ['title','sdetail','detail','cat','status']

        labels={
            'sdetail':'Small Description',
            'detail':'Enter Details',
        }
        catChoices = (('','Select Category'),('1', 'Technical'),('2', 'Travel'),('3', 'Food'))
        
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Post Title'}),
            'sdetail':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Small Description'}),
            'detail':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'cat':forms.Select(choices=catChoices,attrs={'class':'form-select','aria-label':'Default select example'}),
            
        }


class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
