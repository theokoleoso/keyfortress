# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import PassListView, PassCreateView, PassDeleteView, get_decrypted_password

urlpatterns = [
    path("", PassListView.as_view(), name="pass_list"),
    path("create/", PassCreateView.as_view(), name="pass_create"),
    path("delete/<int:pk>/", PassDeleteView.as_view(), name="pass_delete"),
    path("decrypt/", get_decrypted_password, name="decrypt_password"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
