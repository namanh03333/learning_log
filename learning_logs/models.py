from django.db import models
#lm vc vs data 
# Create your models here.
class Topic(models.Model):
    '''Topic user is learning about'''
    #tao cac bang trong database 
    #Bang Topic
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    #Bang Entry
class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ='entries'
    
    def __str__(self):
        if(len(self.text)>50):
            return f"{self.text[:50]}"
        else: 
            return f"{self.text}"