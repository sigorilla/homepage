from django import forms

from blog.models import *

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'intro', 'post', 'tags')