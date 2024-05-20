from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="название")
    preview = models.ImageField(
        upload_to="education/image", **NULLABLE, verbose_name="превью"
    )
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        related_name="courses",
        on_delete=models.SET_NULL,
        **NULLABLE,
        default=None,
        verbose_name="урок",
    )
    title = models.CharField(max_length=150, verbose_name="название")
    preview = models.ImageField(
        upload_to="education/image", **NULLABLE, verbose_name="превью"
    )
    description = models.TextField(verbose_name="описание")
    video_link = models.URLField(**NULLABLE, verbose_name="ссылка на видео")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
