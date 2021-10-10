from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('', views.home, name='home'),
    path('all-news', views.all_news, name='all-news'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('all-category', views.all_category, name='all-categories'),
    path('category/<int:id>', views.category, name='category'),
    path('search-results', views.search_results, name='search-results'),
    path('about', views.about, name='about'),
    path('bios/<int:id>', views.bio, name='bio'),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
