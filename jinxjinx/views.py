from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Jinx, Sentence
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(ListView):
    model = Jinx

class PostCreate(CreateView):
    model = Jinx
    fields = ['title','content',]
    
class SentenceList(ListView):
    model = Sentence
    