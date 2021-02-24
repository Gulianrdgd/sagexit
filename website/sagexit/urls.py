from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/reservations")),
    path("reservations/", include("room_reservation.urls")),
    path("admin/", admin.site.urls),
    path("sso/", include("sp.urls")),
]
