from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

from .views import AddCommentView

urlpatterns = [
    path('', views.Home, name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', views.Blog, name = 'blog'),
    path('<slug:slug>', views.single_post, name='single_post'),
    path('add_comment/', views.AddCommentView.as_view(), name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)