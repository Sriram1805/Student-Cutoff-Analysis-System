from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("dashboard.urls")),
    path("dashboard/", include("user_dashboard.urls")),

    path("calculator/", include("cutoff.urls")),
    path("colleges/", include("colleges.urls")),
    path("prediction/", include("prediction.urls")),
    path("accounts/", include("accounts.urls")),
    path("reports/", include("reports.urls")),
]