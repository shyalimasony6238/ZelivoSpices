from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    HomeBanner,
    About,
    Category,
    Product,
    WhyZelivo,
    SpiceStory,
    Testimonial,
    ContactMessage,
    Newsletter,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "price",
        "weight",
        "is_available",
        "is_featured",
    )

    list_filter = (
        "category",
        "is_available",
        "is_featured",
    )

    search_fields = ("name",)



# ============================================================
# MAINTENANCE MODE
# ============================================================


from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = ("maintenance_mode",)
    list_display_links = None
    list_editable = ("maintenance_mode",)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(HomeBanner)
admin.site.register(About)
admin.site.register(WhyZelivo)
admin.site.register(SpiceStory)
admin.site.register(Testimonial)
admin.site.register(ContactMessage)
admin.site.register(Newsletter)