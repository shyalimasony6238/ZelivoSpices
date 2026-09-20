from django.db import models


# ============================================================
# HOME PAGE
# ============================================================

class HomeBanner(models.Model):
    title = models.CharField(max_length=200)

    subtitle = models.TextField()

    image = models.ImageField(
        upload_to="home/"
    )

    button_text = models.CharField(
        max_length=50,
        default="Explore Products"
    )

    button_link = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return self.title


# ============================================================
# ABOUT US PAGE
# ============================================================

class About(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(
        upload_to="about/"
    )

    mission = models.TextField(
        blank=True
    )

    vision = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.title


# ============================================================
# PRODUCTS PAGE
# ============================================================

class Category(models.Model):
    name = models.CharField(
        max_length=100
    )

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(
        max_length=150
    )

    description = models.TextField(
        blank=True,
        default=""
    )

    image = models.ImageField(
        upload_to="products/"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    weight = models.CharField(
        max_length=50,
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


# ============================================================
# WHY CHOOSE ZELIVO
# ============================================================

class WhyZelivo(models.Model):
    title = models.CharField(
        max_length=100
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True
    )

    image = models.ImageField(
        upload_to="why_zelivo/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


# ============================================================
# SPICE STORY
# ============================================================

class SpiceStory(models.Model):
    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="story/"
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    def __str__(self):
        return self.title


# ============================================================
# TESTIMONIAL
# ============================================================

class Testimonial(models.Model):
    customer_name = models.CharField(
        max_length=100
    )

    review = models.TextField()

    rating = models.PositiveIntegerField(
        default=5
    )

    image = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.customer_name


# ============================================================
# CONTACT MESSAGE
# ============================================================

class ContactMessage(models.Model):
    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    subject = models.CharField(
        max_length=200,
        blank=True
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# ============================================================
# NEWSLETTER
# ============================================================

class Newsletter(models.Model):
    email = models.EmailField(
        unique=True
    )

    subscribed_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.email
