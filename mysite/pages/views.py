from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView
from pages.forms import ContactForm
from pages.models import Article

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Mohammad'
        return context
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
class ArticleListView(ListView):
    model = Article
    template_name = 'pages/article_list.html'
    context_object_name = 'articles'
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'pages/article_detail.html'
    context_object_name = 'article'
class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'
class ThanksPageView(TemplateView):
    template_name = 'pages/thanks.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'pages/article_new.html'
    fields = ['title','content','author']
    success_url = reverse_lazy('article_list')