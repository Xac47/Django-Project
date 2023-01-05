from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .common.views import TitleMixin
from .forms import NewsCreateForm, CommentsPostsForm
from .models import News, Category, CommentsPostsModel, Favorites


class NewsListView(TitleMixin, ListView):
    model = News
    context_object_name = 'news'
    title = 'Главная страница'
    template_name = 'home/home.html'
    ordering = ['-pk']
    paginate_by = 5

    def get_queryset(self):
        queryset = super(NewsListView, self).get_queryset()
        category = self.kwargs.get('category_name')
        return News.objects.filter(category__name=category).order_by('-pk') if category else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(NewsListView, self).get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()

        return ctx


class NewsUserListView(TitleMixin, LoginRequiredMixin, ListView):
    model = News
    context_object_name = 'news'
    title = 'Мои статьи'
    template_name = 'home/news-user.html'
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['pk']) # берет из адресной строки pk
        return News.objects.filter(auther=user).order_by('-pk') if not self.kwargs.get('category_name') else News.objects.filter(auther=user, category__name=self.kwargs['category_name']).order_by('-pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(NewsUserListView, self).get_context_data(**kwargs)
        ctx['user_pk'] = self.kwargs['pk']
        ctx['categories'] = Category.objects.all()

        return ctx



class NewsDetailView(DetailView):
    model = News
    template_name = 'home/news-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])

        return ctx


class NewsCreateView(TitleMixin, LoginRequiredMixin, CreateView):
    model = News
    title = 'Добавление статьи'
    template_name = 'home/news-created.html'
    form_class = NewsCreateForm

    # Автоматический добавляет в models auther пользователя который создал эту статью (или обновил)
    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)


class NewsUpdateView(TitleMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    title = 'Обновить статью'
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


class NewsDeleteView(TitleMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    title = 'Удалить статью'
    template_name = 'home/news-delete.html'
    success_url = '/'
    context_object_name = 'post'

    # Функция проверяет является ли пользователь который хочет обновить статью создателям этой статьи, проверка идет по id
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.auther:
            return True
        return False


@login_required
def favorites_add(request, pk):
    news = News.objects.get(pk=pk)
    favorites = Favorites.objects.filter(user=request.user, post=news)

    if not favorites.exists():
        Favorites.objects.create(user=request.user, post=news).save()
    else:
        favorites.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER']) # возвращает пользователя на ту страницу в котором он совершил данную операция

@login_required
def favorites_list(request, pk, category_name=None):
    if category_name:
        favorites = Favorites.objects.filter(user=pk, post__category__name=category_name).order_by('-pk')
    else:
        favorites = Favorites.objects.filter(user=pk).order_by('-pk')

    context = {
                'favorites_list': favorites,
                'title': 'Избранные',
                'categories': Category.objects.all(),
               }

    return render(request, 'home/news-favorites.html', context)

# class CommentCreateView(CreateView):
#     model = CommentsPostsModel
#     template_name = 'home/create-comment.html'
#     form_class = CommentsPostsForm
#
#     def get_context_data(self, **kwargs):
#         ctx = super(CommentCreateView, self).get_context_data()
#         ctx['post'] = self.kwargs['pk']
#         ctx['comments'] = CommentsPostsModel.objects.filter(post=self.kwargs['pk'])
#         return ctx
#
#     def form_valid(self, form):
#         form.instance.auther, form.instance.post = self.request.user, self.kwargs['pk']
#         return super().form_valid(form)

# def createComment(request, pk):
#     if request.method == 'POST':
#         comments = CommentsPostsModel.objects.filter(post=request.GET['pk'])
#         form = CommentsPostsForm(request.POST['text'], pk, request.user)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CommentsPostsForm()
#         comments = CommentsPostsModel.objects.filter(post=request.GET['pk'])
#         print(request.GET)
#
#     context = {
#         'form': form,
#         'comments': comments,
#     }
#
#     return render(request, 'home/create-comment.html', context)

# class CommentListView(ListView):
#     model = CommentsPostsModel
#     template_name = 'home/list-comment.html'
#     context_object_name = 'comments'
#
#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return CommentsPostsModel.objects.filter(post=pk)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         ctx = super(CommentListView, self).get_context_data()
#         ctx['form'] = CommentsPostsForm()
#
#         return ctx
#
