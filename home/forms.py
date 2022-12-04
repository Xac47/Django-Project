from django import forms

from home.models import News


class NewsCreateForm(forms.ModelForm):
    title = forms.CharField(
        min_length=8,
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

    class Meta:
        model = News
        fields = ['title', 'text']