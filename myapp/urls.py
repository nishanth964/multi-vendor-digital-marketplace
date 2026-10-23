from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='myapp'

urlpatterns = [
    path('', views.index, name='index'),

    path(
        'products/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)