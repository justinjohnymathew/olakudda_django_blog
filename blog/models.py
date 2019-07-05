from django.db import models
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return self.title

     
    def get_absolute_url(self):
        return reverse("blog-detail",args= (self.id,))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
