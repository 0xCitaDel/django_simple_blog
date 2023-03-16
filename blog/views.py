from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
        ListView, 
        DetailView, 
        TemplateView, 
        View, 
        CreateView,
        UpdateView,
        )
from .models import Articles
from .forms import AddForm, BlogViewAuth, BlogViewRegister
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
    
class BlogViewAuth(LoginView):
    form_class = BlogViewAuth
    template_name = "login.html"
    success_url = reverse_lazy('main')
    def get_success_url(self):
        return self.success_url

class BlogViewRegister(CreateView):
    model = User
    form_class = BlogViewRegister
    template_name = 'register.html'
    success_msg = 'Пользователь успешно создан'
    success_url = reverse_lazy('edit_article')

class BlogViewLogOut(LogoutView):
    next_page = reverse_lazy('main')

class ListBlogView(ListView):
    model = Articles
    template_name = 'list_articles.html'
    context_object_name = 'list_articles'

class SingleBlogView(DetailView):
    model = Articles
    template_name = 'single_articles.html'
    context_object_name = 'single_article'

class EditBlogView(LoginRequiredMixin, CreateView):
    model = Articles
    form_class = AddForm
    template_name = 'edit_article.html'
    success_url = reverse_lazy('edit_article')

    def get_context_data(self, **kwargs):
         kwargs['articles_list'] = Articles.objects.all().order_by('-id')
         return super().get_context_data(**kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)

class UpdateBlogView(LoginRequiredMixin, UpdateView):
    model = Articles
    form_class = AddForm
    template_name = 'edit_article.html'
    success_url = reverse_lazy('edit_article')
    
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

def delete_article(request, pk):
     get_object = Articles.objects.get(pk=pk)
     get_object.delete()
     return redirect(reverse('edit_article'))



# class EditBlogView(CreateView):
# ____________________________________________

# def edit_article(request):
#     success = False
#     if request.method == 'POST':
#         form = AddForm(request.POST)
#         if form.is_valid():
#             form.save()
#             success = True


# class UpdateBlogView(UpdateView):
# ____________________________________________

#     articles = Articles.objects.all().order_by('-id')
#     context = {
#         'articles_list': articles,
#         'form': AddForm,
#         'success': success,
#     }
#     return render(request, 'edit_article.html', context)

# def update_article(request, pk):

#     get_article = Articles.objects.get(pk=pk)
#     if request.method == 'POST':
#             form = AddForm(request.POST, instance=get_article)
#             if form.is_valid():
#                 form.save()
#                 success = True
#     context = {
#         'get_article': get_article,
#         'update': True,
#         'form': AddForm(instance=get_article),
#     }
    
#     return render(request, 'edit_article.html', context)
