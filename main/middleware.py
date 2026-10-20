from django.conf import settings
from django.shortcuts import render


class MaintenanceMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if (
            settings.MAINTENANCE_MODE
            and not request.path.startswith("/admin/")
        ):
            return render(
                request,
                "maintenance.html",
                status=503
            )

        return self.get_response(request)

# ============================================================
# MAINTENANCE MODE
# ============================================================

from django.shortcuts import render
from .models import SiteSettings


class MaintenanceMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Always allow Django Admin access
        if request.path.startswith("/admin/"):
            return self.get_response(request)

        # Allow static and media files
        if (
            request.path.startswith("/static/")
            or request.path.startswith("/media/")
        ):
            return self.get_response(request)

        # Check maintenance mode from the database
        settings = SiteSettings.objects.first()

        if settings and settings.maintenance_mode:
            return render(
                request,
                "maintenance.html",
                status=503
            )

        return self.get_response(request)