from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    def create_fields(self):
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.create_fields()

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')