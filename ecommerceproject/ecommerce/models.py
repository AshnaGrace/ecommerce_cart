from django.db import models

# Create your models here.
from django.urls import reverse


class category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
            return reverse('ecommerce:probycat',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)

class product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    desc = models.TextField(blank=True)
    image =models.ImageField(upload_to='product')
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def get_url(self):
            return reverse('ecommerce:proddetail',args=[self.category.slug,self.slug])
    def __str__(self):
        return '{}'.format(self.name)

