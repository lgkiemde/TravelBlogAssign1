from django import forms
from django.forms.widgets import DateInput

from journey.models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'image_url', 'visited_places', 'visited_date', 'favorite_place', 'address', 'favorite_activity',
            'description')
        # Reference - https://stackoverflow.com/questions/41224035/django-form-field-label-how-to-change-its-value-if-it-belongs-to-a-certain-fi
        labels = {'visited_date': "Visited Date"}
        # Reference https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
        widgets = {'visited_date': DateInput(attrs={'type': 'date', 'placeholder': 'Select a date'})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class CreateUserAccountForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, help_text='Required')
    last_name = forms.CharField(max_length=20, help_text='Required')
    email = forms.EmailField(max_length=60, help_text='Required')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')


class ChangePassForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, help_text='Required')
    new_password1 = forms.CharField(max_length=50, help_text='Required')
    new_password2 = forms.CharField(max_length=50, help_text='Required')

    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')
