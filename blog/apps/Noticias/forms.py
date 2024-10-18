from django import forms
from .models import  BlogPost, Categoria


choices = Categoria.objects.all().values_list ('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


     
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug','categoria', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'Categoria': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
            
        }
 