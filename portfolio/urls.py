from django.contrib import admin
from django.urls import path, include
from django.conf import settings # added
from django.conf.urls.static import static # added
import jobs.views # added

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'), # added
    path('blog/', include('blog.urls')), # added. The "blog" in the include function must be the same name with the blog app 42
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # added
