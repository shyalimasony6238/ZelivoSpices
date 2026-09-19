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


admin.site.register(HomeBanner)
admin.site.register(About)
admin.site.register(WhyZelivo)
admin.site.register(SpiceStory)
admin.site.register(Testimonial)
admin.site.register(ContactMessage)
admin.site.register(Newsletter)