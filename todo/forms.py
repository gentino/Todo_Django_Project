from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Tasks


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:outline-none",
            "placeholder": "Enter your email"
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:outline-none",
            "placeholder": "Choose a username"
        })
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:outline-none",
            "placeholder": "Enter password"
        })
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:outline-none",
            "placeholder": "Confirm password"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        """
        Ensure email is unique.
        """
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:outline-none",
            "placeholder": "Enter your username",
            "autofocus": True,
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:outline-none",
            "placeholder": "Enter your password"
        })
    )
    
    



class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Tasks
        fields = ['title','description','done']
        
        
        widgets= {
            'title': forms.TextInput(attrs ={
                'class': 'w-full rounded-lg border border-gray-300 px-4 py-2 focus:ring-2 focous:ring-blue-500 focus:outline-none',
                'placeholder':'Enter task title',
                'required': True,
                
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-lg  border border-gray-300 px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'required': True,
                'placeholder': 'Describe the task to perform'                
            }),
            'done':forms.CheckboxInput(attrs={
                 "class": "h-5 w-5"
            })
        }
        