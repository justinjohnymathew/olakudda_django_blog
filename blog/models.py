from django.db import models
from django.urls import reverse
from django.utils.text import slugify



class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=120,unique=True,editable=False)
    content=models.TextField()
   

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
     
    def get_absolute_url(self):
        return reverse("blog-detail",args= (self.slug,))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
