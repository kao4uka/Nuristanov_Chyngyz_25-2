from django.contrib import admin
from django.urls import path
from products.views import MainPageCBC, ProductsCBV, product_detail_view, CreatePostCBV
from django.conf.urls.static import static
from Blog import settings
from users.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageCBC.as_view()),
    path('products/', ProductsCBV.as_view()),
    path('products/<int:id>/', product_detail_view),
    path('products/create/', CreatePostCBV.as_view()),

    path('users/register/', register_view),
    path('users/login/', login_view),
    path('users/logout/', logout_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
