from django.db import models
from django.urls import reverse

# Create your models here.
class Jinx(models.Model):
    
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
        
class Data(models.Model):
    c = models.CharField(max_length=50, default='')
    n = models.CharField(max_length=50)
    v = models.CharField(max_length=50)
    
    def __str__(self):
        return '[' + self.c + '] ' + self.n + ' ' + self.v
        
    
class Sentence(models.Model):
    cause_noun = models.CharField(max_length=50, default='')
    cause_verb = models.CharField(max_length=50, default='')
    effect_noun = models.CharField(max_length=50, default='')
    effect_verb = models.CharField(max_length=50, default='')

    
    def get_absolute_url(self):
        return reverse('jinxjinx:sentence_list')
    
    def __str__(self):
        return self.cause_noun.__str__()+' '+ self.cause_verb.__str__()+ ' + ' + self.effect_noun.__str__() +' ' + self.cause_verb.__str__()
        
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
        
class Noun(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Verb(models.Model):
    noun = models.ForeignKey(Noun,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Situation(models.Model):
    sentence = models.ForeignKey(Sentence,on_delete=models.CASCADE,related_name='sentence')
    date = models.CharField(max_length=50)
    feeling = models.CharField(max_length=50)
    weather = models.CharField(max_length=50)
    