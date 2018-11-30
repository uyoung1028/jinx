from django.shortcuts import render, resolve_url, redirect
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Jinx, Sentence, Data, Category, Noun, Situation
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q


class jinxbox_view(ListView):
    model = Sentence
    template_name = 'jinxjinx/jinxbox_list.html'

class jinxbox_create(CreateView):
    model = Sentence
    template_name = 'jinxjinx/jinxbox_form.html'
    

# class PostCreate(CreateView):
#     model = Jinx
#     fields = ['title','content',]
    
class SentenceList(ListView):
    model = Sentence
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if str(self.request.user) == "AnonymousUser":
            context['my_sentence_list'] = False
        else:
            my_sentence = Sentence.objects.filter(user=self.request.user)
            context['my_sentence_list'] = my_sentence
        return context
    

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
    # print(name)
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
    # print(name)
    if request.is_ajax():
        noun = Noun.objects.get(name=name)
        print(noun)
        data = {'verb_list':[]}
        for verb in noun.verb_set.all():
            data['verb_list'].append(verb.name)
            # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return redirect(resolve_url('home') )
    
class SentenceCreate(LoginRequiredMixin, CreateView):
    model = Sentence
    fields = ['cause_noun', 'cause_verb', 'effect_noun', 'effect_verb',]
    
    def form_valid(self,form):
        data = self.request.POST
        c
        print(self.request.POST.get('cause_noun'))
        # if Sentence.objects.filter(cause_noun=data.get('cause_noun'))
        # self.object = form.save(commit=False)
        # self.object.user = self.request.user
        # self.object.save()
        
        return super().form_valid(form)
    
    
    