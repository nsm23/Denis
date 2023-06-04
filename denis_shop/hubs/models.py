from django.db import models
from django.urls import reverse


# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=32,
                             blank=True,
                             db_index=True,
                             verbose_name='категория')
    slug_category = models.SlugField(max_length=32,
                                     unique=True,
                                     verbose_name='url')
    sort_order = models.IntegerField(verbose_name='очередность сортировки')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hubs: product_list_by_category ', args=[self.slug_category])
