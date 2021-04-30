from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'web'
urlpatterns = [
    path('', views.base, name='base'),
    path('Anmelden/', views.login_view, name='login'),
    path('registrieren/', views.register_view, name='registration'),
    path('home/', views.logout_view, name='logout'),
    path('anzeige-aufgeben/', views.upload_view, name='posten'),
    path('Anmelden-ok/', views.registrationok_view, name='registration_ok'),
    path('profile/', views.profile_view, name='profile'),
    path('suchen/', views.search, name='search'),
    path('delete/<int:pk>/', views.delete_view, name='delete_post'),
    path('update/<int:pk>', views.update_view, name='update_post'),
    path('detail/<int:pk>/', views.PostDetailView, name='post_detail'),
    path('listview/', views.PostListView.as_view(), name='list_view'),
    path('einkaufen/', views.einkaufenView, name='einkaufen'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
