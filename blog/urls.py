from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('post/cbv/list/', views.PostListView.as_view(), name='post_cbv_list'),
    path('post/cbv/detail/<slug:slug>/', views.PostDetailView.as_view(), name='post_cbv_detail'),
    path('post/cbv/new/', views.PostCreateView.as_view(), name='post_cbv_new'),
    path('post/cbv/edit/<slug:slug>/', views.PostUpdateView.as_view(), name='post_cbv_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)