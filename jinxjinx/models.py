from django.db import models

# Create your models here.
class Jinx(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
        
class Data(models.Model):
    n = models.CharField(max_length=50)
    v = models.CharField(max_length=50)
    
    def __str__(self):
        return self.n + ' / ' + self.v
    
class Sentence(models.Model):
    sen_reason = models.ForeignKey(Data,on_delete=models.CASCADE,related_name='reason')
    sen_result = models.ForeignKey(Data,on_delete=models.CASCADE,related_name='result')
    
    def __str__(self):
        return self.sen_reason.__str__() + ' + ' + self.sen_result.__str__()