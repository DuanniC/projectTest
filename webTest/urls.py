from django.contrib import admin
from django.urls import path
from app.views import home
from app.views import contact
from app.views import login
from app.views import forgotLogin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from rest_framework import routers
from app.views import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home/', home),
                  path('contato/', contact),
                  path('login/', login),
                  path('recuperar/', forgotLogin),
                  path('api/', include(router.urls)),
                  path('', home,),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
