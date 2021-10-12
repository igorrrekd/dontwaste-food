from django.db import models
from django.conf import settings
from location_field.models.plain import PlainLocationField
from django.utils.text import slugify
from django.urls import reverse


class Restaurant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='restaurant_created',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    menu = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,
                               db_index=True)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='restaurant_liked',
                                        blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('restaurant:view')


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name  = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurant:meal_list_by_category', args=[self.slug])


class Meal(models.Model):
    category = models.ForeignKey(Category, related_name='meals',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='meals/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = ["id", "slug"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurant:meal_detail',
                       args=[self.id, self.slug])

