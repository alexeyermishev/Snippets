from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('snippets/add', views.add_snippet_page, name='snippetsadd'),
    path('snippets/list', views.snippets_page, name='snippetslist'),
    path('snippet/<int:snippet_id>/', views.get_snippet, name='snippet'),
    path('snippet/create', views.create_snippet, name='create_snippet'),
    path('snippet/request_del/<int:snippet_id>', views.req_del, name='req_del'),
    path('snippets/delete/<int:snippet_id>', views.delete_snippet, name='delete_snippet'),
    path('snippets/edit/<int:snippet_id>', views.edit_snippet, name='edit_snippet'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),   
    path('my_snippets', views.my_snippets, name='my_snippets'),
    #path('login_page', views.login, name='login_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
