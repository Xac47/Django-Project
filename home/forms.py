from django import forms

from home.models import News, Category, CommentsPostsModel


class NewsCreateForm(forms.ModelForm):
    title = forms.CharField(
        min_length=4,
        max_length=80,
        required=True,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок для статьи'})
    )

    text = forms.CharField(
        min_length=10,
        required=True,
        label='',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание для статьи'})
    )

    category = forms.ModelChoiceField(
        Category.objects.all(),
        label='Категория'
    )


    class Meta:
        model = News
        fields = ('title', 'text', 'category')

class CommentForm(forms.ModelForm):
    text = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарии', 'rows': 4, 'cols': 50})
    )

    class Meta:
        model = CommentsPostsModel
        fields = ('text',)