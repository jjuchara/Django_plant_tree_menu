from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
        verbose_name="parent",
    )
    url = models.CharField(max_length=100, blank=True, verbose_name="url")
    named_url = models.CharField(max_length=100, blank=True, verbose_name="named url")

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        elif self.url:
            return reverse("detail", kwargs={"slug": self.url})
        else:
            return

    class Meta:
        verbose_name = "menu item"
        verbose_name_plural = "menu items"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
