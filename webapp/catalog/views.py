from django.shortcuts import render
from django.views import generic
from django.conf import settings

from .models import Product
from .models import PostProductImage

class ItemDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):

        product = Product.objects.filter(id=self.kwargs['pk'])
        product_id = product[0].id
        images = PostProductImage.objects.filter(product=self.kwargs['pk'])

        context = super(ItemDetailView, self).get_context_data(**kwargs)

        context['page_title'] = f'{str(context["object"])} | карточка товара'
        context['MEDIA_URL'] = settings.MEDIA_URL
        context['images'] = images

        return context

class RenderCatalog(generic.ListView):

    model = Product

    def get_context_data(self, **kwargs):
    
        context = super(RenderCatalog, self).get_context_data(**kwargs)
        
        context['items'] = context['object_list']
        context['MEDIA_URL'] = settings.MEDIA_URL
        context['page_title'] = 'Каталог'
        return context