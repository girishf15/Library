from django.urls import path

from . import views

from libraryapp.settings import DEBUG, MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-book'),
    path('update/<int:book_id>', views.update_book, name='update-book'),
    path('delete/<int:book_id>', views.delete_book, name='delete-book')
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)