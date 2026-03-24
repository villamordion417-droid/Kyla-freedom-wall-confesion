from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-title w-full p-2 rounded bg-slate-800 text-white', 'placeholder': 'Title (optional)'}),
            'content': forms.Textarea(attrs={'class': 'input-content w-full p-2 rounded bg-slate-900 text-white h-40', 'placeholder': 'Share your thought...'}),
        }


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'w-full p-2 rounded bg-slate-800 text-white'}),
        help_text='Required.',
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'w-full p-2 rounded bg-slate-800 text-white'}),
        strip=False,
        help_text='Enter the same password as before, for verification.',
    )


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'w-full p-2 rounded bg-slate-800 text-white'}))
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'w-full p-2 rounded bg-slate-800 text-white'}),
    )
