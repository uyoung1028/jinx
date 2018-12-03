from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

# from django_pandas.io import read_frame
# from django_pandas.managers import DataFrameManager
User = get_user_model()
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
    user = models.ManyToManyField(User,through='UserSentence')
    cause_noun = models.CharField(max_length=50, default='')
    cause_verb = models.CharField(max_length=50, default='')
    effect_noun = models.CharField(max_length=50, default='')
    effect_verb = models.CharField(max_length=50, default='')

    
    def get_absolute_url(self):
        return reverse('jinxjinx:sentence_list')
    
    def __str__(self):
        return self.cause_noun.__str__()+' '+ self.cause_verb.__str__()+ ' + ' + self.effect_noun.__str__() +' ' + self.cause_verb.__str__()

class UserSentence(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sentence = models.ForeignKey(Sentence,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.sentence.__str__() + ' / ' + self.user.__str__()

        
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
    
# class Situation(models.Model):
#     sentence = models.ForeignKey(Sentence,on_delete=models.CASCADE,related_name='sentence')

    
class Comment(models.Model):
    sentence = models.ForeignKey(UserSentence, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    # content = models.TextField()
    date = models.DateField(max_length=50)
    weather = models.CharField(max_length=50)
    feeling = models.CharField(max_length=50)
    result = models.BooleanField(max_length=50)    

    def __str__(self):
        return self.sentence.__str__()
        
    def get_absolute_url(self):
        return reverse('jinxjinx:usersentence_detail', kwargs={'pk': self.sentence_id})

# class DataAnalaysis(models.Model):
    
# qs = Sentence.objects.all()
# df = read_frame(qs)
# df = read_fram(qs, fieldnames=['cause_noun', 'cause_verb', 'effect_noun', 'effect_verb'])
