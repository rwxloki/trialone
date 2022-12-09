from django.db import models
from django.urls import reverse #new

class Mymod(models.Model):
    text = models.TextField()

    def __str__(self): 
        return self.text[:50]
#blogmodel
class BlogMod(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):#new
        return reverse('mydetail', args=[str(self.id)])
