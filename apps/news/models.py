from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Sarlavha"))
    image = models.ImageField(upload_to="post_pictures/%B/", blank=True, null=True)
    body = models.TextField(blank=True, null=True, verbose_name=_("1 - Qism"))
    image2 = models.ImageField(upload_to="post_pictures/%B/", blank=True, null=True)
    body2 = models.TextField(blank=True, null=True, verbose_name=_("2 - Qism"))
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("posts:post_details", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.title} : {self.created_at}"

    def get_second_image(self):
        return self.image2.url if self.image2 else None

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Yangiliklar"
        verbose_name = "Yangilik"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="product_images/")
    image2 = models.ImageField(upload_to="product_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def get_first_image(self):
        return self.image.url if self.image else None
    
    def get_second_image(self):
        return self.image2.url if self.image2 else None

    class Meta:
        verbose_name_plural = "Maxsulotlar"
        verbose_name = "Maxsulot"

class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=(("new", "Yangi"), ("read", "Ko'rilgan")), default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name