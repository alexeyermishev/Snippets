from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('snippets/add', views.add_snippet_page, name='snippetsadd'),
    path('snippets/list', views.snippets_page, name='snippetslist'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
