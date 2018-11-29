from django.shortcuts import render, resolve_url, redirect
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Jinx, Sentence, Data, Category, Noun
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.http import HttpResponse

class PostList(ListView):
    model = Jinx

class PostCreate(CreateView):
    model = Jinx
    fields = ['title','content',]
    
class SentenceList(ListView):
    model = Sentence
    

class DataList(ListView):
    model = Data
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['data_list_unique'] = Data.objects.values('c').distinct() 
        return context
        
class CategoryList(ListView):
    model = Category
    
def category_noun(request):
    name = request.POST.get('name')
    if request.is_ajax():
        catagory = Category.objects.get(name=name)
        data = {'noun_list':[]}
        for noun in catagory.noun_set.all():
            data['noun_list'].append(noun.name)
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return redirect( resolve_url('home') )
        
class NounList(ListView):
    model = Noun
    
def noun_verb(request):
    name = request.POST.get('name')
    if request.is_ajax():
        noun = Noun.objects.get(name=name)
        data2 = {'verb_list':[]}
        for verb in noun.verb_set.all():
            data['verb_list'].append(verb.name)
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return redirect( resolve_url('home') )