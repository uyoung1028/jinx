from django.shortcuts import render, resolve_url, redirect
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Jinx, Sentence, Data, Category, Noun, Situation, UserSentence
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
        cause_noun = self.request.POST.get('cause_noun')
        cause_verb = self.request.POST.get('cause_verb')
        effect_noun = self.request.POST.get('effect_noun')
        effect_verb = self.request.POST.get('effect_verb')
        sentences = Sentence.objects.filter(Q(cause_noun=cause_noun)&Q(cause_verb=cause_verb)&Q(effect_noun=effect_noun)&Q(effect_verb=effect_verb))
        already = sentences.exists()
        # print(filter)
        if already:
            print("이미있음")
            if UserSentence.objects.filter(Q(user=self.request.user)&Q(sentence=sentences[0])).exists():
                print("사용자가 있는문장 등록")
                # 사용자가 이미 등록해놓은 문장이 있으면 그 문장으로 가야됨
                return redirect(resolve_url('home'))  # 나중에는 디테일페이지로
            else:
                #이미 등록해놓은 문장이 있으면 usersentence에 저장하고 그 문장으로 이동
                usersentence = UserSentence.objects.create(user=self.request.user, sentence=sentences[0])
                return redirect(resolve_url('home'))
        else:
            print("없음")
            # self.object = form.save(commit=False)
            # self.object.user = self.request.user
            form.save()
            UserSentence.objects.create(user=self.request.user, sentence=sentences[0])
            return super().form_valid(form)
    
    
    