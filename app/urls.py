
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from produtos.views import ProdutoListView, ProdutoDetailView
from usuarios.views import RegisterView, login_view, logout_view
from .views import HomeView

urlpatterns = [
    path('admin/'              ,  admin.site.urls),
    path(''                    ,  HomeView.as_view(),          name='home'),
    path('produtos/'           ,  ProdutoListView.as_view(),   name='lista_produtos'),
    path('produtos/<int:pk>/'  ,  ProdutoDetailView.as_view(), name='produto_detail'),
    path('register/'           ,  RegisterView.as_view(),      name='register'),
    path('login/'              ,  login_view,                  name='login'),
    path('logout/'             ,  logout_view,                 name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
