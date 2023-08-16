import uuid

from django.urls import reverse
from django.db import models
from django.db.models import QuerySet

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('catalog:category_detail_view', args=[str(self.id)])

class Mark(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('catalog:model_detail_view', args=[str(self.id)])

class Product(models.Model):
  
    def upload_to(self, *args):
        image_path = f'product_images/{uuid.uuid4()}.jpeg'
        return image_path

    def generate_name(self):
        return f'{self.mark} {self.model}'
    
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    mark = models.ForeignKey(
        'Mark', on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=200, db_index=True)
    engine_capacity = models.PositiveIntegerField()
    drive_unit = models.CharField(max_length=200, db_index=True)
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('catalog:item_detail_view', args=[str(self.id)])

    def get_preview(self):
        product_images: QuerySet[PostProductImage] = PostProductImage.objects.filter(product=self.id)
        return product_images[0] if len(product_images) > 0 else ''

    def __str__(self) -> str:
        return f'{self.mark} {self.model}'

class PostProductImage(models.Model):

  def upload_to(self, *args) -> str:
    image_path = f'product_images/{uuid.uuid4()}.jpeg'
    return image_path

  product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
  images = models.FileField(upload_to=upload_to)

  def __str__(self) -> str:
    return str(self.images)