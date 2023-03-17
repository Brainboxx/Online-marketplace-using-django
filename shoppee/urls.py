from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core.views import index, contact, signup
from core.forms import LogInForm
from items.urls import views

urlpatterns = [
    path('', index, name='index'),
    path('items', include('items.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LogInForm), name='login'),
    path('new/', views.new, name='new'),
    path('inbox/', include('conversation.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/index.html'), name='logout'),
    path('new/', views.new, name='new'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
