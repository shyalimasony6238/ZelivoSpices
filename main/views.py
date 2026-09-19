from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import (
    HomeBanner,
    About,
    Category,
    Product,
    SpiceStory,
    Testimonial,
    ContactMessage,
)


def home(request):

    banner = HomeBanner.objects.first()

    featured_products = Product.objects.filter(
        is_featured=True,
        is_available=True
    )[:8]

    testimonials = Testimonial.objects.all()[:6]

    context = {
        "banner": banner,
        "featured_products": featured_products,
        "testimonials": testimonials,
    }

    return render(
        request,
        "home.html",
        context
    )


def about(request):

    about = About.objects.first()

    return render(
        request,
        "about.html",
        {
            "about": about
        }
    )


def products(request):

    categories = Category.objects.all()

    products = Product.objects.all()

    context = {
        "categories": categories,
        "products": products,
    }

    return render(
        request,
        "products.html",
        context
    )
from django.shortcuts import render, redirect
from .forms import ProductForm


def add_product(request):

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('products')

    else:

        form = ProductForm()

    return render(
        request,
        'add_product.html',
        {'form': form}
    )



def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    return render(
        request,
        "product_detail.html",
        {
            "product": product
        }
    )


def story(request):

    stories = SpiceStory.objects.all()

    return render(
        request,
        "story.html",
        {
            "stories": stories
        }
    )


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")

        email = request.POST.get("email")

        phone = request.POST.get("phone")

        subject = request.POST.get("subject")

        message = request.POST.get("message")


        ContactMessage.objects.create(

            name=name,

            email=email,

            phone=phone,

            subject=subject,

            message=message

        )


        messages.success(
            request,
            "Thank you! Your message has been received."
        )


        return redirect("contact")


    return render(
        request,
        "contact.html"
    )
def privacy(request):
    return render(
        request,
        "privacy.html"
    )