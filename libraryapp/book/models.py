from django.db import models

# Create your models here.

class Book(models.Model):

    name = models.CharField(max_length=50)
    picture = models.ImageField()
    authour = models.CharField(max_length=30, default='anonymous')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='Heyyy this books belongs to girish')

    def __repr__(self):
        return repr(self.name)
