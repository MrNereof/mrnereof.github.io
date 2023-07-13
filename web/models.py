from django.db import models
from ckeditor.fields import RichTextField


class Painting(models.Model):
    class Meta:
        verbose_name = "Картина"
        verbose_name_plural = "Картины"

    name = models.CharField(max_length=50, verbose_name="Название")
    author = models.CharField(max_length=50, verbose_name="Автор")
    image = models.ImageField(upload_to="paintings", verbose_name="Изображение")

    def __str__(self):
        return self.name


class Project(models.Model):
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    slug = models.SlugField(default="", null=False, blank=True)
    name = models.CharField(max_length=50, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to="projects", blank=True, verbose_name="Изображение")
    link = models.URLField(blank=True, verbose_name="Ссылка")
    priority = models.IntegerField(blank=True, default=100, verbose_name="Приоритет")

    def __str__(self):
        return self.name

