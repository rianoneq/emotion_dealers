from django.urls import path
from . import views
from django.urls import re_path

app_name = 'catalog'

urlpatterns = [
    re_path(r'^$', views.RenderCatalog.as_view(),
            name='catalog'),
]
# urlpatterns += [
#     re_path(r'^item/(?P<pk>[-\w]+)/$', views.ItemDetailView.as_view(),
#             name='item_detail_view'),
# ]
urlpatterns += [
    re_path(r'^item/(?P<pk>[-\w]+)/$', views.detail_view,
            name='item_detail_view'),
]
