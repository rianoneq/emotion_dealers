from django.shortcuts import render
from django.views import generic
from django.conf import settings

from .models import Product
from .models import PostProductImage
from django.template.loader import render_to_string
from django.http import HttpResponse

def detail_view(request, pk: int):
    # if request.is_ajax():
    product = Product.objects.filter(id=pk)

    images = PostProductImage.objects.filter(product=pk)
    if len(product) < 1:
        return HttpResponse(status=404)
    html = render_to_string('catalog/product_detail.html', {'product': product[0], 'images': images, 'MEDIA_URL': settings.MEDIA_URL})
    res = HttpResponse(html)
    res.__setitem__("Content-type", "html")
    res.__setitem__("Access-Control-Allow-Origin", "*")
    return res

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