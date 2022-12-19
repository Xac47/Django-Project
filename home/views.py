from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import NewsCreateForm
from .models import News


class NewsListView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'home/home.html'
    ordering = ['-pk']
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(NewsListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница'

        return ctx


class NewsUserListView(LoginRequiredMixin, ListView):
    model = News
    context_object_name = 'news'
    template_name = 'home/news-user.html'
    paginate_by = 5


    def get_queryset(self):
        # из ссылки забирает id и присваивает к переменной user,
        user = get_object_or_404(User, pk=self.kwargs['id'])
        # потом возвращает все статьи где auther равен тому id который мы передаем через переменную user, и под конец сортирует по убывание id все статьи
        return News.objects.filter(auther=user).order_by('-pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(NewsUserListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Мои статьи'
        ctx['count'] = len(News.objects.filter(auther=self.kwargs['id']))

        return ctx



class NewsDetailView(DetailView):
    model = News
    template_name = 'home/news-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])

        return ctx


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'home/news-created.html'
    # fields = ['title', 'text']
    form_class = NewsCreateForm

    # Автоматический добавляет в models auther пользователя который создал эту статью (или обновил)
    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(NewsCreateView, self).get_context_data(**kwargs)
        ctx['title'] = 'Добавление статьи'

        return ctx

class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'home/news-update.html'
    # fields = ['title', 'text']
    form_class = NewsCreateForm

    # Функция проверяет является ли пользователь который хочет обновить статью создателям этой статьи, проверка идет по id
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.auther:
            return True
        return False

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(NewsUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = 'Обновить статью'

        return ctx


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'home/news-delete.html'
    success_url = '/'
    context_object_name = 'post'

    # Функция проверяет является ли пользователь который хочет обновить статью создателям этой статьи, проверка идет по id
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.auther:
            return True
        return False


    def get_context_data(self, **kwargs):
        ctx = super(NewsDeleteView, self).get_context_data(**kwargs)
        ctx['title'] = 'Удалить статью'

        return ctx
