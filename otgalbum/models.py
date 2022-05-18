from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.conf import settings

class Oblast(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Область')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='SLUG')

    def get_absolute_url(self):
        return reverse_lazy('oblast', kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = 'Області'
        verbose_name = 'Область'
        ordering = ['id']

    def __str__(self):
        return self.name

class Gromada(models.Model):
    TYPE_CHOICES = [
        ('міська', 'міська'),
        ('селищна', 'селищна'),
        ('сільська', 'сільська'),
    ]

    oblast = models.ForeignKey(Oblast, related_name='gromada', on_delete=models.CASCADE, verbose_name='Область')
    title = models.CharField(max_length=255, verbose_name='Назва')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='SLUG')
    tg_type = models.CharField(choices=TYPE_CHOICES, max_length=255, verbose_name='Тип')
    area = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Площа')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Запис створено')

    def get_absolute_url(self):
        return reverse_lazy('gromada_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = 'Громади'
        verbose_name = 'Громада'
        ordering = ['title']

    def __str__(self):
        return self.title

class Geoportal(models.Model):
    TYPE_GEOPORTAL = [
        ('Публічний', 'Публічний'),
        ('Службовий', 'Службовий'),
    ]
    gromada = models.ForeignKey(Gromada, related_name='geoportal', on_delete=models.CASCADE, verbose_name='Громада')
    type_geoportal = models.CharField(choices=TYPE_GEOPORTAL, max_length=255, verbose_name='Тип доступу')
    portal_url = models.URLField(max_length=400, blank=True, verbose_name='Посилання на геопортал')
    image = models.ImageField(upload_to='images/', default='images/default.jpg', verbose_name='Зображення')
    created_for = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='Користувач', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активний')
    views = models.IntegerField(verbose_name='Переглядів', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Запис створено')

    class Meta:
        verbose_name_plural = 'Геопортали'
        verbose_name = 'Геопортал'
        ordering = ['gromada']

    def get_absolute_url(self):
        return reverse_lazy('by_oblast', kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.gromada)