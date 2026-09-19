from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "about/",
        views.about,
        name="about"
    ),

    path(
        "products/",
        views.products,
        name="products"
    ),
        path(
        'addproduct/',
        views.add_product,
        name='add_product'
    ),

    path(
        "products/<int:pk>/",
        views.product_detail,
        name="product_detail"
    ),

    path(
        "our-story/",
        views.story,
        name="story"
    ),

    path(
        "contact/",
        views.contact,
        name="contact"
    ),
    path(
        "privacy/",
        views.privacy,
        name="privacy"
    )
]