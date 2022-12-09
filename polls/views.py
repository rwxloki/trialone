#from django.shortcuts import render

'''from django.http import HttpResponse


def  home(request):
    return HttpResponse('Hello')
    '''
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #new
from .models import BlogMod, Mymod #added this
#added listView had previously used templateview
from django.urls import reverse_lazy

#class HomePage (TemplateView):
class HomePage (ListView):
    model = Mymod
    template_name = 'home.html'
    context_object_name = 'object_list'#new


class AboutPage (TemplateView):
    template_name = 'about.html'


class BlogPage(ListView):
    model = BlogMod
    template_name = 'blog.html'
    context_object_name = 'my_object_list'#new

class DetailPage(DetailView):
    model = BlogMod
    template_name = 'detail.html'
    context_object_name = 'my_object'
    #by defailt detailview will provide a context object which is either modelsname in small letter or the word object
    #this view also expects either a primary key or a slug passed to it as the identifier
    #you can explicitly name context object though

class CreatePage(CreateView):
    model = BlogMod
    template_name = 'new.html'
    fields = ['title', 'author', 'body']

class EditPage(UpdateView):
    model = BlogMod
    template_name = 'edit.html'
    fields = ['title', 'body']

class DeletePage(DeleteView):
    model = BlogMod
    template_name = 'delete.html'
    success_url = reverse_lazy('myhome')